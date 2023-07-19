from __future__ import annotations

import argparse

import cv2
import glob
import numpy as np
import pickle

from .camera import Camera

NUM_CALIBRATION_IMAGES = 10


class Calibrator:
    def __init__(self):
        self.ret = None
        self.camera_matrix = None
        self.dist = None
        self.rot_vecs = None
        self.tran_vecs = None

    def save_calibration(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @staticmethod
    def load_calibration(filename) -> Calibrator:
        with open(filename, 'rb') as file:
            return pickle.load(file)

    def calibrate(self, camera=None, filename_format=None):
        chessboard_size = (9, 6)
        frame_size = (2448, 2048)

        # termination criteria
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

        # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
        objp = np.zeros((chessboard_size[0] * chessboard_size[1], 3), np.float32)
        objp[:, :2] = np.mgrid[0:chessboard_size[0], 0:chessboard_size[1]].T.reshape(-1, 2)

        size_of_chessboard_squares_mm = 20
        objp = objp * size_of_chessboard_squares_mm

        # Arrays to store object points and image points from all the images.
        obj_points = []  # 3d point in real world space
        img_points = []  # 2d points in image plane.

        if filename_format:
            images = glob.glob(filename_format)
            if len(images) < NUM_CALIBRATION_IMAGES:
                print(f'Warning using less than {NUM_CALIBRATION_IMAGES}, calibration may be inaccurate')
        else:
            images = []
            cam = Camera() if camera is None else camera

            input(f"Start calibration ({NUM_CALIBRATION_IMAGES} images)? <Press ENTER>")
            for i in range(NUM_CALIBRATION_IMAGES):
                print(f'Taking image {i}')
                for attempt in range(3):
                    try:
                        img = cam.get_image()
                        images.append(img)
                        scale = 0.5
                        cv2.imshow('Image', cv2.resize(img, (int(img.shape[1] * scale), int(img.shape[0] * scale))))
                        cv2.waitKey(2000)
                        break
                    except AssertionError:
                        if attempt == 3:
                            print('Error getting image')
                        else:
                            continue
                if i == NUM_CALIBRATION_IMAGES:
                    break
                input("Ready for next image? <Press ENTER>")

        for image in images:

            img = cv2.imread(image) if type(image) is str else image

            # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Find the chess board corners
            ret, corners = cv2.findChessboardCorners(img, chessboard_size, None)

            # If found, add object points, image points (after refining them)
            if ret:
                obj_points.append(objp)
                corners2 = cv2.cornerSubPix(img, corners, (11, 11), (-1, -1), criteria)
                img_points.append(corners)

                # Draw and display the corners
                cv2.drawChessboardCorners(img, chessboard_size, corners2, ret)
                # cv2.imshow('img', img)
                # cv2.waitKey(5000)

        cv2.destroyAllWindows()

        ret, camera_matrix, dist, rot_vecs, tran_vecs = cv2.calibrateCamera(obj_points, img_points, frame_size, None, None)
        self.ret = ret
        self.camera_matrix = camera_matrix
        self.dist = dist
        self.rot_vecs = rot_vecs
        self.tran_vecs = tran_vecs

        # Reprojection Error
        mean_error = 0

        for i in range(len(obj_points)):
            img_points2, _ = cv2.projectPoints(obj_points[i], self.rot_vecs[i], self.tran_vecs[i], self.camera_matrix,
                                               self.dist)
            error = cv2.norm(img_points[i], img_points2, cv2.NORM_L2) / len(img_points2)
            mean_error += error

        print("total error: {}".format(mean_error / len(obj_points)))

    def undistort_image(self, image):
        img = cv2.imread(image)
        h, w = img.shape[:2]
        new_camera_matrix, roi = cv2.getOptimalNewCameraMatrix(self.camera_matrix, self.dist, (w, h), 1, (w, h))

        # Undistort
        dst = cv2.undistort(img, self.camera_matrix, self.dist, None, new_camera_matrix)

        # crop the image
        x, y, w, h = roi
        dst = dst[y:y + h, x:x + w]
        cv2.imwrite('undistorted1.jpg', dst)

        # Undistort with Remapping
        mapx, mapy = cv2.initUndistortRectifyMap(self.camera_matrix, self.dist, None, new_camera_matrix, (w, h), 5)
        dst = cv2.remap(img, mapx, mapy, cv2.INTER_LINEAR)

        # crop the image
        x, y, w, h = roi
        dst = dst[y:y + h, x:x + w]
        cv2.imwrite('undistorted1.jpg', dst)

    def get_camera_params(self):
        fx = self.camera_matrix[0][0]
        fy = self.camera_matrix[1][1]
        cx = self.camera_matrix[0][2]
        cy = self.camera_matrix[1][2]
        return [fx, fy, cx, cy]


def calibrate_distance(camera=None, known_distance=-1, filename=None):
    if filename:
        image = filename
    else:
        cam = Camera() if camera is None else camera

        input("Start distance calibration? <Press ENTER>")
        print(f'Taking image')
        for attempt in range(3):
            try:
                image = cam.get_image()
                scale = 50
                cv2.imshow('Image', cv2.resize(image, (image.shape[1] * scale / 100, image.shape[0] * scale / 100)))
                cv2.waitKey(2000)
                break
            except AssertionError:
                if attempt == 3:
                    print('Error getting image')
                else:
                    continue

    if known_distance == -1:
        while True:
            try:
                known_distance = int(input("Enter marker distance (cm):"))
                break
            except ValueError:
                print("Please enter a number")

    img = cv2.imread(image) if type(image) is str else image


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Program that calibrates a camera using OpenCV checkerboard")
    parser.add_argument('filename', help='File to save calibration instance in')
    calibrator = Calibrator()
    calibrator.calibrate()
    filename_arg = parser.parse_args().filename
    print(f"Saving calibration to {filename_arg}")
    calibrator.save_calibration(filename_arg)
