import argparse

import cv2

import camera.camera as camera
from camera import Calibrator
from camera.detector import Detector

parser = argparse.ArgumentParser(description="Program that detects april tags from an image")
parser.add_argument('-c', '--camera', action='store_true', help='Use the Basler GbE camera as the input',
                    required=False)
args = parser.parse_args()

if args.camera:
    cam = camera.Camera(color=False, auto=False)
    print("Getting image")
    img = cam.get_image()
    cam.close_camera()
    if img is None:
        exit(2)
else:
    img = cv2.imread('images/marker_1500mm.png', cv2.IMREAD_GRAYSCALE)

print(img.shape)
cv2.namedWindow("Camera Test", cv2.WINDOW_NORMAL)
cv2.imshow('Camera Test', img)

cv2.waitKey(5000)

cv2.destroyAllWindows()


# print("RUNNING CALIBRATION")
# camera_matrix = camera.calibrate_camera(cam, 'images/calibrate*.jpg')
# print("COMPLETED CALIBRATION")

tag_size = 0.04     # 4 cm
# calibrator = Calibrator()
print("Loading calibration")
calibrator = Calibrator.load_calibration('calibration_10.pickle')
# calibrator.calibrate(filename_format='images/calibrate*.jpg')
detector = Detector(tag_size)
print("Detecting tags")
tags = detector.detect(img, calibrator)

if len(tags) > 0:
    print(tags[0])
    distance = max(max(tags[0].pose_t[0][-1], tags[0].pose_t[1][-1]), tags[0].pose_t[2][-1])
    print(f"Distance is {distance:.2f}")
    # calculate_distance(tags[-1], 11, 100)
else:
    print("No tags found!")
