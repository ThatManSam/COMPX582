#!/home/joelshep/documents/university/COMPX582/camera/catkin_ws/venv/bin/python3

import os
import numpy as np
import yaml
import rospy
from test_get_image.msg import ImageBundle # type: ignore
import cv2 as cv

from camera.detector import Detector
from camera.calibrate import Calibrator

window_name = "Camera Test"

def ProcessImages(image, args):
    if not isinstance(args[0], Detector):
        print("Argument is not a detector")
        return
    
    detector: Detector = args[0]
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
    print(f"\rFound tags: {' | '.join([str(tag.tag_id) for tag in tags]) if len(tags) > 0 else 'None'}", end="")
    cv.namedWindow(window_name, cv.WINDOW_NORMAL)
    cv.imshow(window_name, overlayed)
    # cv.imshow(window_name, bw_image)
    cv.waitKey(1)

if __name__ == '__main__':
    rospy.init_node("test_get_camera")

    print(f"CWD {os.getcwd()}")
    # img = cv.imread('../../images/calibrate1.jpg')
    camera_config_file = './src/test_get_image/CameraConfigs/basler_1L.yaml'
    with open(camera_config_file, 'rt') as file:
        camera_config = yaml.safe_load(file)
    print(camera_config)
    cam_matrix = camera_config["camera_matrix"]["data"]
    camera_matrix = np.array(camera_config['camera_matrix']['data']).reshape(3, 3)
    dist_coeffs = np.array(camera_config['distortion_coefficients']['data'])
    image_width = camera_config['image_width']
    image_height = camera_config['image_height']
    
    
    
    
    calibration = Calibrator(camera_config.camera_matrix.data)
    
    detector = Detector(14)
    
    rospy.loginfo("[PLAIN PY NODE] namespace of node = " + rospy.get_namespace())
    rospy.Subscriber("/baslerimages", ImageBundle, ProcessImages, (detector, ))
    rospy.spin()
    cv.destroyAllWindows()
