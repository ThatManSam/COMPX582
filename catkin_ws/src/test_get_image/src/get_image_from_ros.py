#!/usr/bin/env python3

from math import sqrt
from blessed import Terminal # type: ignore

import os
import threading
import numpy as np
import yaml
import rospy
from test_get_image.msg import ImageBundle # type: ignore
import queue
import cv2 as cv

from camera.detector import Detector
from camera.calibrate import Calibrator

window_name = "Camera Test"

image_queue = queue.Queue(2)

def ReceiveImages(image):
    try:
        image_queue.put_nowait(image)
    except queue.Full:
        # Don't store old images
        pass

def ProcessImages(det: Detector, term=None):
    while not rospy.is_shutdown():
        image = image_queue.get()
        term = term
        detector: Detector = det
        
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
        img_flipped = cv.rotate(img_uint8, cv.ROTATE_180) # type: ignore
        # print(f'Width: {img.width} | Height: {img.height} | Data Count: {len(img.data)} | Encoding: {img.encoding} | Shape: {img_flipped.shape}')
        
        # calibration = Calibrator()
        
        bw_image = cv.cvtColor(img_flipped, cv .COLOR_BGR2GRAY)
        tags = detector.detect(bw_image)
        # for tag in tags:
        #     print(f"Tag found, ID: {tag.tag_id} | type: {type(tag.tag_id)}")
        overlayed = detector.overlay_tags(img_flipped, tags, input_color=True)
        
        if term is not None:
            print(term.clear())
            # Display the list of tags at the bottom left
            
            with term.location(0, term.height - len(tags) - 2):
                if len(tags) == 0:
                    print("No Tags Found")
                else:
                    tag = tags[0]
                    if tag.pose_t is not None:
                        x = tag.pose_t[0][-1]/100
                        y = tag.pose_t[1][-1]/100
                        z = tag.pose_t[2][-1]/100
                        dist = sqrt(x**2 + y**2 + z**2)
                        
                        # Extract the first row (or first column) of the rotation matrix
                        camera_orientation = tag.pose_R[0, :]

                        # Calculate the angle left or right (in radians) relative to the camera's orientation
                        angle_left_right = np.arctan2(camera_orientation[2], camera_orientation[0])
                        
                        angle_left_right_degrees =  np.degrees(angle_left_right)

                        x_adjusted = z * np.sin(angle_left_right)
                        z_adjusted = z * np.cos(angle_left_right)

                        # x_rounded = int(round(x))
                        x_rounded = int(round(x_adjusted))
                        y_rounded = int(round(y))
                        # z_rounded = int(round(z))
                        z_rounded = int(round(z_adjusted))
                        
                        # Center the status page
                        with term.location(0, term.height // 2 - 5):
                            # Display right/left distance (90 degrees to forward)
                            # print(term.center(f"Right/Left Distance: {x:.3f} m ({x_adjusted:.3f})"))
                            print(term.center(f"Right/Left Distance: {x_adjusted:.3f} m ({x:.3f})"))
                            
                            x_scaled = x_rounded*2
                            # Create a horizontal line of "-" for the forward distance
                            print(term.center(" "*x_scaled + "—" * abs(x_scaled) + " "*-x_scaled))
                            
                            # Create vertical lines of "|" for the right/left distance
                            for _ in range(z_rounded):
                                print(term.center("|"))
                            # print(term.center(f"Forward Distance: {z:.3f} m ({z_adjusted:.3f})"))
                            print(term.center(f"Forward Distance: {z_adjusted:.3f} m ({z:.3f})"))
                            print(term.center(f"Angle (degs): {angle_left_right: .2f}°"))
                    for tag in tags:
                        if tag.pose_t is not None:
                            x = tag.pose_t[0][-1]
                            y = tag.pose_t[1][-1]
                            z = tag.pose_t[2][-1]
                            dist = sqrt(x**2 + y**2 + z**2)
                            print(f"\rTime: {image.header.stamp.secs}, ID: {tag.tag_id}, {f'Distance: F {z: .2f} R {x: .2f} Abs {dist.real: .2f}cm' if dist is not None else ''}{' '*20}", end="")
                            # print(f"ID: {tag.tag_id}, Distance: {dist}")
        else:
            if len(tags) == 0:
                print(f"\rNo Tags Found, Time: {image.header.stamp.secs}" + " "*40, end="")
            for tag in tags:
                if tag.pose_t is not None:
                    x = tag.pose_t[0][-1]
                    y = tag.pose_t[1][-1]
                    z = tag.pose_t[2][-1]
                    dist = sqrt(x**2 + y**2 + z**2)
                    # Extract the first row (or first column) of the rotation matrix
                    camera_orientation = tag.pose_R[0, :]

                    # Calculate the angle left or right (in radians) relative to the camera's orientation
                    angle_left_right = np.arctan2(camera_orientation[2], camera_orientation[0])

                    # Convert the angle from radians to degrees
                    angle_left_right_degrees = np.degrees(angle_left_right)
                    print(f"\rTime: {image.header.stamp.secs}, ID: {tag.tag_id}, {f'Distance: F {z: .2f} R {x: .2f} Abs {dist.real: .2f}cm' if dist is not None else ''}{' '*20} Angle {angle_left_right_degrees}°", end="")
                    # print(f"ID: {tag.tag_id}, Distance: {dist}")
                else:
                    print(f"\rTime: {image.header.stamp.secs}, ID: {tag.tag_id}", end="")
        cv.namedWindow(window_name, cv.WINDOW_NORMAL)
        cv.imshow(window_name, overlayed)
        # cv.imshow(window_name, bw_image)
        cv.waitKey(1)
        
        
def calculate_direction():
    pass
    
if __name__ == '__main__':
    rospy.init_node("test_get_camera")
    rospy.loginfo("[PLAIN PY NODE] namespace of node = " + rospy.get_namespace())

    print(f"CWD {os.getcwd()}")
    # img = cv.imread('../../images/calibrate1.jpg')
    print("Loading camera config")
    camera_config_file = './src/test_get_image/CameraConfigs/basler_1L.yaml'
    with open(camera_config_file, 'rt') as file:
        camera_config = yaml.safe_load(file)
    # print(camera_config)
    cam_matrix = camera_config["camera_matrix"]["data"]
    camera_matrix = np.array(camera_config['camera_matrix']['data']).reshape(3, 3)
    dist_coeffs = np.array(camera_config['distortion_coefficients']['data'])
    
    calibration = Calibrator(camera_matrix, dist=dist_coeffs)
    detector = Detector(14, calibrator=calibration)

    print("Ready")

    term = Terminal()
    # term = None
    with term.fullscreen(), term.cbreak():
        rospy.Subscriber("/baslerimages", ImageBundle, ReceiveImages)
        
        thread = threading.Thread(target=ProcessImages, args=(detector, term))
        thread.start()
        # rospy.spin()
        thread.join()
        rospy.signal_shutdown("Closing")
    cv.destroyAllWindows()
