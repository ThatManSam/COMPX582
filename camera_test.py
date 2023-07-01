import cv2
import camera.camera as camera

cam = camera.Camera(color=True)

print("RUNNING CALIBRATION")
camera.calibrate_camera(cam, 'images/calibrate*.jpg')
print("COMPLETED CALIBRATION")

img = cam.get_image()

cv2.namedWindow("Camera Test", cv2.WINDOW_NORMAL)
cv2.imshow('Camera Test', img)

cv2.waitKey(5000)

cv2.destroyAllWindows()

cam.close_camera()
