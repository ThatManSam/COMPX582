#!/usr/bin/env python3

from math import sqrt
from typing import Optional
from blessed import Terminal # type: ignore

import argparse
import os
import threading
import numpy as np
import yaml
from camera import camera
import rospy
import queue
import cv2 as cv

from simple_pid import PID
from geometry_msgs.msg import Twist
from camera.detector import Detector
from camera.calibrate import Calibrator

class Driver:
    def __init__(self, Kp, Ki, Kd, target, active=True, publisher: Optional[rospy.Publisher]=None, serial=None) -> None:
        if active and publisher is None and serial is None:
            raise ValueError("Cannot have active driver without publisher or serial")
        self.pub = publisher
        self.last_x = 0
        self.last_z = 0
        self.active = active
        
        self.pid = PID(Kp, Ki, Kd, setpoint=target)
        
        self._diff_check_thresh = 0.5 # 0.5 a metre
        
        self.FACTOR_SPEED = 1
        self.FACTOR_TURN = 1
        
        self.MAX_SPEED = 1.0
        self.MAX_TURN = 1.0
        self.STOP_DIST = 2
        self.RATIO_TURN_SPEED = 0.5
        
    def _stabalise_sign(self, side, forward):
        stab_side = side
        if side > self._diff_check_thresh:
            diff = abs(side - self.last_x)
            if diff > abs(max(side, self.last_x)):
                stab_side = -side
                
        stab_forward = abs(forward) # Forward is always positive (cart can't look backwardss)
        self.last_x = stab_side
        self.last_z = stab_forward
        return stab_side, stab_forward
        
    def receive_telemetry(self, side, forward):
        real_side, real_forward = self._stabalise_sign(side, forward)
        print(f"Stabalised: side: {real_side:.3f} for: {real_forward:.3f}")
        if real_forward < self.STOP_DIST:
            self.update_drive(0, 0)
            return
        pid_side = self.pid(real_side)
        print(f"Direct PID out: {pid_side:.3f}")
        if pid_side is None:
            print('Error with PID calucation')
            return
        pid_turn = (pid_side - self.pid.setpoint)*self.MAX_TURN
        if pid_turn > 0:
            pid_turn = min(pid_turn, self.MAX_TURN)
        else:
            pid_turn = max(pid_turn, -self.MAX_TURN)
        pid_forward = self.MAX_SPEED - pid_turn*self.RATIO_TURN_SPEED
        
        self.update_drive(pid_forward, pid_turn)
        
    def update_drive(self, forward, turn):
        f_forward = forward * self.FACTOR_SPEED
        f_turn = turn * self.FACTOR_TURN
        print(f"Sending output: f: {f_forward:.3f} | t: {f_turn:.3f}")
        self.twist = self._create_twist(f_forward, f_turn)
        if self.active:
            self.pub.publish(self.twist)
        else:
            print(repr(self))
        
    def _create_twist(self, forward, turn) -> Twist:
        t = Twist()
        t.linear.x = forward
        t.angular.z = turn
        return t
    
    def __repr__(self) -> str:
        return (
            'linear: {self.twist.linear.x:.3f}\n'
            'angular: {self.twist.angular.z:.3f}'
        ).format(self=self)

window_name = "Camera Test"

image_queue = queue.Queue(1)

term: Optional[Terminal] = None

def ReceiveImages(image):
    try:
        image_queue.put_nowait(image)
    except queue.Full:
        # Don't store old images
        pass


def obtain_image(image):
    Images = image.Images
    # print(f"Images headers {image.header}")
    # print(f"Images LLH {image.LLH}")
    # print(f"Images Device IDs {image.DeviceIDs}")
    img = Images[0]
    
    # print(img.data)
    # print(f"Array Sizes: Expected: {img.height*img.width*3} | Actual: {len(img.data)}")
    img_array_data = np.frombuffer(img.data, dtype=np.uint8)
    
    img_array = np.array(img_array_data, dtype=np.uint8).reshape(img.height, img.width, 3)

    # Convert the image array to uint8 type (expected by OpenCV)
    img_uint8 = np.uint8(img_array)
    # cv.imwrite("ROS_INPUT.jpg", img_uint8)
    img_flipped = cv.rotate(img_uint8, cv.ROTATE_180) # type: ignore
    # print(f'Width: {img.width} | Height: {img.height} | Data Count: {len(img.data)} | Encoding: {img.encoding} | Shape: {img_flipped.shape}')
    return img_flipped

# def show_stats(term, x_rd, z_rd, x_ad, z_ad, x, z, angle, rot_calced, area, other_calced):
def show_stats(term, x, z, area):
    if term is None:
        print("Can't show stats, no display")
        return
    # Center the status page
    with term.location(0, term.height // 2 - 5):
        # Display right/left distance (90 degrees to forward)
        # print(term.center(f"Right/Left Distance: {x:.3f} m ({x_adjusted:.3f})"))
        # print(term.center(f"Right/Left Distance: {x_ad:.3f} m ({x:.3f})"))
        print(term.center(f"Right/Left Distance: {x:.3f} m"))
        # x_scaled = x_rd*2
        x_scaled = -int(round(x))*2
        # Create a horizontal line of "-" for the forward distance
        print(term.center(" "*x_scaled + "—" * abs(x_scaled) + " "*-x_scaled))
        
        # Create vertical lines of "|" for the right/left distance
        # for _ in range(z_rd):
        for _ in range(abs(int(round(z)))):
            print(term.center("|"))
        # print(term.center(f"Forward Distance: {z:.3f} m ({z_adjusted:.3f})"))
        # print(term.center(f"Forward Distance: {z_ad:.3f} m ({z:.3f})"))
        print(term.center(f"Forward Distance: {z:.3f} m"))
        # print(term.center(f"Angle (degs): {angle: .2f}°"))
        print(term.center(f"Area: {area: .2f}"))
        # print(term.center(f"Angles (degs): X: {rot_x: .2f}° Y: {rot_y: .2f}° Z: {rot_z: .2f}°"))
        # print(term.center(f"Angles\n{rot_calced[0]}\n{rot_calced[1]}\n{rot_calced[2]}\n"))
        # print(term.center(f"Angles X\n{other_calced['x'][0]}\n{other_calced['x'][1]}"))
        # print(term.center(f"Angles Y\n{other_calced['y'][0]}\n{other_calced['y'][1]}"))
        # print(term.center(f"Angles Z\n{other_calced['z'][0]}\n{other_calced['z'][1]}"))
        # print(term.center(f"Average X {other_calced['avg']['x']:.2f} Y {other_calced['avg']['y']:.2f} Z {other_calced['avg']['z']:.2f}"))

def calc_pose_opencv(tag, det, image, term=None):
    
    if tag.pose_t is not None:
        # if det.calibrator is not None:
        #     draw_vectors(tag, det, image)
            
        t_vec, R_vec = invert_matrices(tag.pose_t, tag.pose_R)
        
        # x = tag.pose_t[0][-1]/100
        # y = tag.pose_t[1][-1]/100
        # z = tag.pose_t[2][-1]/100
        
        x = t_vec[0][-1]/100
        y = t_vec[1][-1]/100
        z = t_vec[2][-1]/100
        
        dist = sqrt(x**2 + y**2 + z**2)
        
        # # Extract the first row (or first column) of the rotation matrix
        # camera_orientation = tag.pose_R[0, :]

        # # Calculate the angle left or right (in radians) relative to the camera's orientation
        # angle_left_right = np.arccos(camera_orientation[0])
        
        # rot_calced = [[f"{np.degrees(np.arccos(ang)): .2f}°" for ang in row] for row in tag.pose_R]
        # other_calced = {
        #     "x": [
        #         [np.degrees(np.arccos(tag.pose_R[1, 1])), np.degrees(-1*np.arcsin(tag.pose_R[1, 2]))],
        #         [np.degrees(np.arcsin(tag.pose_R[2, 1])), np.degrees(np.arccos(tag.pose_R[2, 2]))]
        #     ],
        #     "y": [
        #         [np.degrees(np.arccos(tag.pose_R[0, 0])), np.degrees(np.arcsin(tag.pose_R[0, 2]))],
        #         [np.degrees(-1*np.arcsin(tag.pose_R[2, 0])), np.degrees(np.arccos(tag.pose_R[2, 2]))]
        #     ],
        #     "z": [
        #         [np.degrees(np.arccos(tag.pose_R[0, 0])), np.degrees(-1*np.arcsin(tag.pose_R[0, 1]))],
        #         [np.degrees(np.arcsin(tag.pose_R[1, 0])), np.degrees(np.arccos(tag.pose_R[1, 1]))]
        #     ]
        # }
        
        # avg_other_calced = {
        #     "x": (abs(other_calced['x'][0][0]) + abs(other_calced['x'][0][1]) + abs(other_calced['x'][1][0]) + abs(other_calced['x'][1][1]))/4,
        #     "y": (abs(other_calced['y'][0][0]) + abs(other_calced['y'][0][1]) + abs(other_calced['y'][1][0]) + abs(other_calced['y'][1][1]))/4,
        #     "z": (abs(other_calced['z'][0][0]) + abs(other_calced['z'][0][1]) + abs(other_calced['z'][1][0]) + abs(other_calced['z'][1][1]))/4,
        # }
        
        # other_calced['avg'] = avg_other_calced
        
        # angle_left_right_degrees =  np.degrees(angle_left_right)

        # x_adjusted = z * np.sin(angle_left_right)
        # z_adjusted = z * np.cos(angle_left_right)
        # x_adjusted, z_adjusted = calculate_adjustment(z, x, angle_left_right)
        # # x_rounded = int(round(x))
        # x_rounded = int(round(x_adjusted))
        # y_rounded = int(round(y))
        # # z_rounded = int(round(z))
        # z_rounded = int(round(z_adjusted))
        area = calc_area(tag.corners)
        # show_stats(term, x_rounded, z_rounded, x_adjusted, z_adjusted, x, z, angle_left_right_degrees, rot_calced, area, other_calced)
        # show_stats(term, x, z, area)
        return x, y, z, area
    else:
        print("Can't calculate pose")
        return None, None, None, None
        

def calc_area(c):
    x1 = c[0, 0]
    x2 = c[1, 0]
    x3 = c[2, 0]
    x4 = c[3, 0]
    y1 = c[0, 1]
    y2 = c[1, 1]
    y3 = c[2, 1]
    y4 = c[3, 1]
    
    # From https://www.themathdoctors.org/polygon-coordinates-and-areas/#:~:text=If%20the%20points%20are%20(x1,right%20and%20divide%20by%202.)
    area = abs(0.5 * ((x1*y2-x2*y1) + (x2*y3-x3*y2) + (x3*y4-x4*y3) + (x4*y1-x1*y4)))
    return area

def calc_pose_dist(tag, image, term=None):
    if tag.pose_t is not None:
        x = tag.pose_t[0][-1]/100
        y = tag.pose_t[1][-1]/100
        z = tag.pose_t[2][-1]/100
        
        dist = sqrt(x**2 + y**2 + z**2)
        
        middle = image.shape[0]/2
        
        pos = (tag.corners[0, 0] + tag.corners[2, 0])/2
        
        error = middle - pos
        area = calc_area(tag.corners)
        return error, dist, area
    return None, None, None

def invert_matrices(t, R):
    R_inv = np.linalg.inv(R)
    t_inv = -np.dot(R_inv, t)
    return t_inv, R_inv

def draw_vectors(tag, det, img):
    # Draw the vectors
    axis = np.float32([[3,0,0], [0,3,0], [0,0,-3]]).reshape(-1,3) # type: ignore

    imgpts, jac = cv.projectPoints(axis, tag.pose_R, tag.pose_t, det.calibrator.camera_matrix, det.calibrator.dist)

    def draw(img, corners, imgpts):
        def to_int(x):
            return int(x)
        
        corner = tuple(corners[0].ravel())
        corner = tuple(map(lambda p: int(p), corner))
        print(f"Point to print: {corner}")
        img = cv.line(img, corner, tuple(map(to_int, imgpts[2].ravel())), (0,0,255), 5)
        img = cv.line(img, corner, tuple(map(to_int, imgpts[0].ravel())), (255,0,0), 5)
        img = cv.line(img, corner, tuple(map(to_int, imgpts[1].ravel())), (0,255,0), 5)
        return img
        
    overlayed = draw(img,tag.corners,imgpts)
    return overlayed

def ProcessImages(det: Detector, driver: Driver, term=None, stop_event=None, ros=True, active_output=False, straight=False, area=False):
    if not stop_event:
        stop_event = threading.Event()
    
    while not stop_event.is_set():
        try:
            image = image_queue.get(timeout=1)
        except queue.Empty:
            continue
        term = term
        detector: Detector = det
        if ros:
            img_flipped = obtain_image(image)
            bw_image = cv.cvtColor(img_flipped, cv.COLOR_BGR2GRAY)
            # cv.imwrite("ROS_PROCESSED.jpg", bw_image)
        else:
            img_flipped = image
            bw_image = image
        
        # calibration = Calibrator()
        tags = detector.detect(bw_image)
        # for tag in tags:
        #     print(f"Tag found, ID: {tag.tag_id} | type: {type(tag.tag_id)}")
        
        overlayed = detector.overlay_tags(img_flipped, tags, input_color=ros)
        
        if term is not None:
            print(term.clear())
            # Display the list of tags at the bottom left
            
            with term.location(0, term.height - len(tags) - 2):
                if len(tags) == 0:
                    print("No Tags Found")
                else:
                    for tag in tags:
                        if tag.pose_t is not None:
                            # if straight or area:
                            side, dist, meas_area = calc_pose_dist(tag, overlayed, term)
                            if side is None or dist is None or area is None:
                                continue
                            # if area:
                            #     # driver.receive_telemetry(side, meas_area)
                            #     print(f"ID: {tag.tag_id}, Distance: Area {meas_area: .2f} Side {side: .2f}{' '*20}", end="")
                            # else:
                                # driver.receive_telemetry(side, dist)
                            print(f"ID: {tag.tag_id}\n")
                            print(f"Calc: Abs {dist: .2f} Side {side: .2f} Area {meas_area: .2f}")
                            # else:
                            x, y, z, area = calc_pose_opencv(tag, det, overlayed, term)
                            if x is None or y is None or z is None or area is None:
                                continue
                            # driver.receive_telemetry(x, z)
                            # x = tag.pose_t[0][-1]
                            # y = tag.pose_t[1][-1]
                            # z = tag.pose_t[2][-1]
                            dist = sqrt(x**2 + y**2 + z**2)
                            # print(f"\rTime: {image.header.stamp.secs if ros else 'None'}, ID: {tag.tag_id}, {f'Distance: F {z: .2f} R {x: .2f} Abs {dist.real: .2f}cm' if dist is not None else ''}{' '*20}", end="")
                            r_x = pose_side_calc(x)
                            r_z = pose_straight_calc(z)
                            r_side = pixel_side_calc(side, z)
                            
                            print(f"Pose: {f'F {z: .4f} R {x: .4f}' if dist is not None else 'Error'}")
                            print(f"SIDE: {r_side: .2f} POSE: STRAIGHT: {r_z:.2f} SIDE: {r_x:.2f}")
                            # print(f"ID: {tag.tag_id}, Distance: {dist}")
                
        else:
            if len(tags) == 0:
                print(f"\rNo Tags Found, Time: {image.header.stamp.secs if ros else 'None'}" + " "*40, end="")
            for tag in tags:
                if tag.pose_t is not None:
                    x, y, z, area = calc_pose_opencv(tag, det, overlayed, term)
                    if x is None or y is None or z is None or area is None:
                        continue
                    driver.receive_telemetry(x, z)
                    # x = tag.pose_t[0][-1]
                    # y = tag.pose_t[1][-1]
                    # z = tag.pose_t[2][-1]
                    dist = sqrt(x**2 + y**2 + z**2)
                    # # Extract the first row (or first column) of the rotation matrix
                    # camera_orientation = tag.pose_R[0, :]

                    # # Calculate the angle left or right (in radians) relative to the camera's orientation
                    # angle_left_right = np.arctan2(camera_orientation[2], camera_orientation[0])

                    # # Convert the angle from radians to degrees
                    # angle_left_right_degrees = np.degrees(angle_left_right)
                    print(f"\rTime: {image.header.stamp.secs if ros else 'None'}, ID: {tag.tag_id}, {f'Distance: F {z: .2f} R {x: .2f} Abs {dist.real: .2f}cm' if dist is not None else ''}{' '*20}", end="")
                    # print(f"ID: {tag.tag_id}, Distance: {dist}")
                else:
                    print("No pose estimated")
                    print(f"\rTime: {image.header.stamp.secs if ros else 'None'}, ID: {tag.tag_id}", end="")
        cv.namedWindow(window_name, cv.WINDOW_NORMAL)
        cv.imshow(window_name, overlayed)
        # cv.imshow(window_name, bw_image)
        cv.waitKey(1)
        

def pixel_side_calc(m_side, dist):
    m_side_sign = 1 if m_side >= 0 else -1
    m_side_abs = abs(m_side)
    
    s = 741.23/545.25
    
    d = abs(dist) + 3
    
    b = -0.1632*pow(d, 2) + 1.1553*d
    
    side = m_side_abs/(741.23*pow(s, -b))
    
    return side*m_side_sign

def pose_straight_calc(dist):
    return 1.03*abs(dist)-0.4

def pose_side_calc(side):
    return side/1.59

def calculate_direction():
    pass

def calculate_adjustment(a, b, angle) -> tuple:
    # Calculating camera position based on marker perspective

    t = b/np.tan((np.pi/2) - angle)
    s = a - t
    y = s * np.cos(angle)
    
    # Similar triangles
    p = b*s/y
    q = y*t/b
    
    x = p+q
    return x, y
    
def run_ros(args):
    from test_get_image.msg import ImageBundle # type: ignore
    rospy.init_node("test_get_camera", disable_signals=True)

    print(f"CWD {os.getcwd()}")
    # img = cv.imread('../../images/calibrate1.jpg')
    print("Loading camera config")
    camera_config_file = './src/test_get_image/CameraConfigs/basler_1L.yaml'
    with open(camera_config_file, 'rt') as file:
        camera_config = yaml.safe_load(file)
    # print(camera_config)
    camera_matrix = np.array(camera_config['camera_matrix']['data']).reshape(3, 3)
    dist_coeffs = np.array(camera_config['distortion_coefficients']['data'])
    
    calibration = Calibrator(camera_matrix, dist=dist_coeffs)
    detector = Detector(args.size, calibrator=calibration)

    pub = rospy.Publisher("/twist", Twist, queue_size=1)

    driver = Driver(0.2, 0.05, 0.02, 4, False, pub) # OpenCV
    # driver = Driver(0.5, 0.2, 0.1, 2, False, pub) # Other

    print("Ready")

    term = Terminal()
    # term = None
    if term is not None:
        with term.fullscreen(), term.cbreak():
            rospy.Subscriber("/baslerimages", ImageBundle, ReceiveImages)
            event = threading.Event()
            thread = threading.Thread(
                target=ProcessImages,
                args=(detector, driver, term, event),
                kwargs={
                    'ros':True,
                    'active_output':False,
                    'straight':False,
                    'area':False}
                )
            thread.start()
            try:
                event.wait()
            except KeyboardInterrupt:
                event.set()
    else:
        rospy.Subscriber("/baslerimages", ImageBundle, ReceiveImages)
        event = threading.Event()
        thread = threading.Thread(
            target=ProcessImages,
            args=(detector, driver, term, event),
            kwargs={
                'ros':True,
                'active_output':False,
                'straight':False,
                'area':False}
            )
        thread.start()
        try:
            event.wait()
        except KeyboardInterrupt:
            event.set()
    print("Closing")
    thread.join()
    rospy.signal_shutdown("Closing")
    
    cv.destroyAllWindows()


def continuous_camera_capture(event: threading.Event):
    cam = camera.Camera(color=False, auto=False)
    while not event.is_set():
        try:
            image_queue.put_nowait(cam.get_image())
        except queue.Full:
            # Don't store old images
            pass
    cam.close_camera()

def run_local(args):
    print("Loading camera config")
    if args.calibration == 'base':
        camera_config_file = './src/test_get_image/CameraConfigs/basler_1L.yaml'
        with open(camera_config_file, 'rt') as file:
            camera_config = yaml.safe_load(file)
        cam_matrix = camera_config["camera_matrix"]["data"]
        camera_matrix = np.array(camera_config['camera_matrix']['data']).reshape(3, 3)
        dist_coeffs = np.array(camera_config['distortion_coefficients']['data'])
        calibration = Calibrator(camera_matrix, dist=dist_coeffs)
    elif args.calibration == '20':
        calibration = Calibrator.load_calibration('../calibration_20.pickle')
    else:
        raise ValueError("Invalid calibration")
    dist = args.mode == 'dist'
    area = args.mode == 'area'

    pub=None
    
    pid_default = (0.2, 0.05, 0.02)

    kp, ki, kd = args.pid if args.pid else pid_default

    driver = Driver(kp, ki, kd, args.target, False, pub) # OpenCV
    # driver = Driver(0.5, 0.2, 0.1, 2, False, pub) # Other
    
    detector = Detector(args.size, calibrator=calibration)
    term = Terminal()
    # term = None
    with term.fullscreen(), term.cbreak():        
        event = threading.Event()
        print("Starting processing")
        process_thread = threading.Thread(
            target=ProcessImages,
            args=(detector, driver, term, event, False, dist, area)
        )
        process_thread.start()
        print("Starting Capture")
        capture_thread = threading.Thread(target=continuous_camera_capture, args=(event,))
        capture_thread.start()
        try:
            event.wait()
        except KeyboardInterrupt:
            event.set()
    print("Closing")
    process_thread.join()
    capture_thread.join()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='AprilTag Navigation',
        description='Drives a motor based on AprilTags detected by a camera'
    )
    parser.add_argument('-r', '--ros', action='store_true', help='Enables camera input from ros (Surbey Robot)')
    parser.add_argument('-s', '--size', help='Set the marker size for detection (default 9)', default=9.0, type=float)
    parser.add_argument('-m', '--mode', choices=['dist', 'area'], help='Set the measuring mode (default pose)', default=None)
    parser.add_argument('-t', '--target', help='Set the target for PID controller (default 2)', default=2)
    parser.add_argument('-p', '--pid', nargs=3, help='Set the k values for PID controller')
    parser.add_argument('-c', '--calibration', choices=['base', '20'], help='Set camera calibration (default base)', default='base')
    
    args = parser.parse_args()
    if args.ros:
        run_ros(args)
    else:
        run_local(args)