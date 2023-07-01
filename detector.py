import argparse
import os
import sys
from time import sleep
import cv2
from dt_apriltags import Detector

from camera.camera import Camera

images = []


def run_from_camera():
    at_detector = Detector(families='tagStandard52h13',
                           nthreads=1,
                           quad_decimate=1.0,
                           quad_sigma=0.0,
                           refine_edges=1,
                           decode_sharpening=0.25,
                           debug=0)

    output_folder = 'camera_test'

    camera = Camera()

    img = camera.get_image()

    # scale = 1
    # img = cv2.resize(img, (0,0), fx=scale, fy=scale)

    # cv2.imshow(f'Looking in image {image}', cv2.resize(img, (540, 960)))
    # cv2.waitKey(0)
    # sleep(2)
    # cv2.destroyAllWindows()
    tags = at_detector.detect(img)  # Detecting the tag

    color_img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)

    for tag in tags:
        for idx in range(len(tag.corners)):
            cv2.line(color_img, tuple(tag.corners[idx - 1, :].astype(int)), tuple(tag.corners[idx, :].astype(int)),
                     (0, 255, 0), 5)

        cv2.putText(color_img, str(tag.tag_id),
                    org=(tag.corners[0, 0].astype(int) + 10, tag.corners[0, 1].astype(int) + 10),
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=0.8,
                    color=(0, 0, 255))

    # cv2.imshow(f'Detected tags for image {image}', cv2.resize(color_img, (540, 960)))
    # cv2.waitKey(0)
    # sleep(2)
    # cv2.destroyAllWindows()
    output_path = os.path.join('output', output_folder)
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    if not cv2.imwrite(os.path.join(output_path, "test.png"), color_img):
        print(f"DIDN'T SAVE test.png")


def run_from_file():
    at_detector = Detector(families='tagStandard52h13',
                           nthreads=1,
                           quad_decimate=1.0,
                           quad_sigma=0.0,
                           refine_edges=1,
                           decode_sharpening=0.25,
                           debug=0)

    input_folder = ''
    output_folder = 'gap_test'

    # images = [file for file in os.listdir(input_folder)]
    images = ['./tag52_13_00006_bordered_close.png', './tag52_13_00006_bordered_gap.png']

    for image in images:
        print(f'Processing: {image}')
        img = cv2.imread(os.path.join(input_folder, image), cv2.IMREAD_GRAYSCALE)

        if img is None:
            print("ERROR: Image is none")
            continue

        # scale = 1
        # img = cv2.resize(img, (0,0), fx=scale, fy=scale)

        # cv2.imshow(f'Looking in image {image}', cv2.resize(img, (540, 960)))
        # cv2.waitKey(0)
        # sleep(2)
        # cv2.destroyAllWindows()
        tags = at_detector.detect(img)  # Detecting the tag

        color_img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)

        for tag in tags:
            for idx in range(len(tag.corners)):
                cv2.line(color_img, tuple(tag.corners[idx - 1, :].astype(int)), tuple(tag.corners[idx, :].astype(int)),
                         (0, 255, 0), 5)

            cv2.putText(color_img, str(tag.tag_id),
                        org=(tag.corners[0, 0].astype(int) + 10, tag.corners[0, 1].astype(int) + 10),
                        fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                        fontScale=0.8,
                        color=(0, 0, 255))

        # cv2.imshow(f'Detected tags for image {image}', cv2.resize(color_img, (540, 960)))
        # cv2.waitKey(0)
        # sleep(2)
        # cv2.destroyAllWindows()
        output_path = os.path.join('output', output_folder)
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        if not cv2.imwrite(os.path.join(output_path, image), color_img):
            print(f"DIDN'T SAVE {image}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Program that detects april tags from an image")
    parser.add_argument('-c', '--camera', action='store_true', help='Use the Basler GbE camera as the input',
                        required=False)

    args = parser.parse_args()

    if args.camera:
        run_from_camera()
    else:
        run_from_file()
