#!/home/joelshep/documents/university/COMPX582/camera/catkin_ws/venv/bin/python3

import numpy as np
import rospy
from test_get_image.msg import ImageBundle # type: ignore
import cv2 as cv

from camera.detector import Detector
from camera.calibrate import Calibrator


def ProcessImages(image, args):
    if not isinstance(args[0], Detector):
        print("Argument is not a detector")
        return
    
    detector: Detector = args[0]
    Images = image.Images
    print(f"Images headers {image.header}")
    print(f"Images LLH {image.LLH}")
    print(f"Images Device IDs {image.DeviceIDs}")
    img = Images[0]
    
    # print(img.data)
    print(f"Array Sizes: Expected: {img.height*img.width*3} | Actual: {len(img.data)}")
    img_array_data = np.frombuffer(img.data, dtype=np.uint8)
    
    img_array = np.array(img_array_data, dtype=np.uint8).reshape(img.height, img.width, 3)

    # Convert the image array to uint8 type (expected by OpenCV)
    img_uint8 = np.uint8(img_array)
    img_flipped = cv.rotate(img_uint8, cv.ROTATE_180) # type: ignore
    
    calibration = Calibrator()
    
    tags = detector.detect(img_flipped, calibration)
    
    print(f'Width: {img.width} | Height: {img.height} | Data Count: {len(img.data)} | Encoding: {img.encoding}')
    cv.imshow(window_name, img_flipped)
    cv.waitKey(1)

if __name__ == '__main__':
    rospy.init_node("test_get_camera")

    # img = cv.imread('../../images/calibrate1.jpg')
    window_name = "Camera Test"
    cv.namedWindow(window_name, cv.WINDOW_NORMAL)
    # cv.imshow(window_name, img)
    # cv.waitKey(1)

    detector = Detector(14)
    
    rospy.loginfo("[PLAIN PY NODE] namespace of node = " + rospy.get_namespace())
    rospy.Subscriber("/baslerimages", ImageBundle, ProcessImages, (detector, ))
    rospy.spin()
    cv.destroyAllWindows()
