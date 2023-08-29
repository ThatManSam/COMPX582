import argparse
import os.path

import cv2
import numpy

import camera.camera as camera
from camera import Calibrator
from camera.detector import Detector

parser = argparse.ArgumentParser(description="Program that detects april tags from an image")
parser.add_argument('size', help='Marker Size')
parser.add_argument('distance', nargs='?', default=-1, help='Distance to Marker')
parser.add_argument('offset', nargs='?', default='0', help='Horizontal distance offset (-ve for left, +ve for right')

args = parser.parse_args()

size = int(args.size)
distance = float(args.distance)
offset = float(args.offset)

distances = [
    # 1,
    # 2,
    # 3,
    # 4,
    # 5,
    6,
    7,
    8
] if distance == -1 else [distance]

for dist in distances:
    args_string = f"{size} cm tag @ {dist:.1f} m, offset {offset:.1f} m"

    cam = camera.Camera(auto=False)
    print(f"Getting image {args_string}")
    img = cam.get_image()
    cam.close_camera()
    if img is None:
        exit(2)

    print(f"Shape: {img.shape}")

    # window_name = f"Image {args_string}"
    # cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    # cv2.imshow(window_name, img)
    # cv2.waitKey()
    # cv2.destroyAllWindows()

    detector = Detector(size)
    print("Detecting tags")
    calibrator = Calibrator.load_calibration('calibration_20.pickle')
    tags = detector.detect(img, calibration=calibrator)
    output_path = os.path.join('output', 'lab_exp_cal10')

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    if len(tags) <= 0:
        print("No tags found!")
        window_name = f"NO TAGS Image {args_string}"
        cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
        cv2.imshow(window_name, img)
        cv2.waitKey()
        cv2.destroyAllWindows()
    for tag in tags:
        color_img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
        for idx in range(len(tag.corners)):
            cv2.line(color_img, tuple(tag.corners[idx-1, :].astype(int)), tuple(tag.corners[idx, :].astype(int)),
                     (0, 255, 0), 1)

        cv2.putText(color_img, str(tag.tag_id),
                    org=(tag.corners[0, 0].astype(int)-20, tag.corners[0, 1].astype(int)+20),
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=1.2,
                    color=(0, 0, 255),
                    thickness=1)

        print(f"Found tag ID: {tags[0].tag_id}")

        distance = ('X', tags[0].pose_t[0][-1])
        if distance[1] < tags[0].pose_t[1][-1]:
            distance = ('Y', tags[0].pose_t[1][-1])
        if distance[1] < tags[0].pose_t[2][-1]:
            distance = ('Z', tags[0].pose_t[2][-1])
        factor = 151
        offset = -41.213
        real = (distance[1] - offset)/factor
        rad_offsetX = numpy.rad2deg(tags[0].pose_R[0][0])
        rad_offsetY = numpy.rad2deg(tags[0].pose_R[1][1])
        rad_offsetZ = numpy.rad2deg(tags[0].pose_R[2][2])
        rad_offset = tags[0].pose_R[1][2]
        print(f"Distance \n\treal: {real:.2f}m\n\tmeasured: {distance[1]:.2f}\n\t"
              f"Degree: X:{rad_offsetX:.3f} Y:{rad_offsetY:.3f} Z:{rad_offsetZ:.3f}")

        window_name = f"Image {args_string}"
        cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
        cv2.imshow(window_name, color_img)
        cv2.waitKey()
        cv2.destroyAllWindows()

        cv2.imwrite(os.path.join(output_path, f"tag_{size}cm_{dist:.1f}m_{offset:.1f}d.jpg"), color_img)
