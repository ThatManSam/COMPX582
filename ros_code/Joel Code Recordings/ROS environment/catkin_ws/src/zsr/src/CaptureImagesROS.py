#!/usr/bin/python3

import pypylon.pylon as py
import time
import cv2
import rospy
from std_msgs.msg import String
from zsr.msg import ImageBundle
from cv_bridge import CvBridge

bridge = CvBridge()

def ImagePublisher():
    baslerImages = rospy.Publisher('/baslerimages', ImageBundle, queue_size=100)
    #rospy.init_node('ImageCapture', anonymous=True)
    rate = rospy.Rate(FPS)
    while not rospy.is_shutdown():
        #try:
        CapturedImages = ["No Image"]*len(CameraIDs)
        CurrentTime = time.time()
        TriggerCam.ExecuteSoftwareTrigger() #Execute Software Trigger on main camera
        while any(Frame == "No Image" for Frame in CapturedImages):
            with cam_array.RetrieveResult(1000) as res:
                if res.GrabSucceeded():
                    cam_id = res.GetCameraContext()
                    CapturedImages[cam_id] = res.Array
                    #print("Image captured from " + str(cam_id))
            res.Release()
        msg = ImageBundle()
        msg.DeviceIDs = []
        for i in range(0,len(CameraIDs)):
            msg.Images.append(bridge.cv2_to_imgmsg(cv2.cvtColor(CapturedImages[i], cv2.COLOR_BAYER_RG2RGB), "bgr8"))
            msg.DeviceIDs.append(String(CameraIDs[i]))
        # msg.Images[0] = bridge.cv2_to_imgmsg(cv2.cvtColor(CapturedImages[0], cv2.COLOR_BAYER_RG2RGB), "bgr8")
        # msg.Images[1] = bridge.cv2_to_imgmsg(cv2.cvtColor(CapturedImages[1], cv2.COLOR_BAYER_RG2RGB), "bgr8")
        # msg.Images[2] = bridge.cv2_to_imgmsg(cv2.cvtColor(CapturedImages[2], cv2.COLOR_BAYER_RG2RGB), "bgr8")
        # msg.Images[3] = bridge.cv2_to_imgmsg(cv2.cvtColor(CapturedImages[3], cv2.COLOR_BAYER_RG2RGB), "bgr8")
        # msg.Images[4] = bridge.cv2_to_imgmsg(cv2.cvtColor(CapturedImages[4], cv2.COLOR_BAYER_RG2RGB), "bgr8")
        # msg.Images[5] = bridge.cv2_to_imgmsg(cv2.cvtColor(CapturedImages[5], cv2.COLOR_BAYER_RG2RGB), "bgr8")
        msg.header.stamp = rospy.Time.from_sec(CurrentTime)
        # msg.DeviceIDs = [String(CameraIDs[0]),String(CameraIDs[1]),String(CameraIDs[2]),String(CameraIDs[3]),String(CameraIDs[4]),String(CameraIDs[5])]
        baslerImages.publish(msg)
        print("\nImages Pushed at " + str(CurrentTime))
        #except:
            #print("Error occured capturing images")
        rate.sleep()

def StartCameras():
    global TriggerCam, cam_array, CameraIDs, FPS
    rospy.init_node('ImageCapture', anonymous=True)
    CameraIDs = rospy.get_param("~CameraIDs")
    FPS = rospy.get_param("~FPS")
    tlf = py.TlFactory.GetInstance()
    di = py.DeviceInfo()
    devs = tlf.EnumerateDevices([di,])
    cam_array = py.InstantCameraArray(len(CameraIDs))
    for idx, cam in enumerate(cam_array):
        cam.Attach(tlf.CreateDevice(devs[idx]))
    cam_array.Open()
    for i in range(0,len(CameraIDs)):
        if cam_array[i].DeviceInfo.GetUserDefinedName() == CameraIDs[0]:
            TriggerCam = cam_array[i]
        cam_array[i].SetCameraContext(i)
        cam_array[i].UserSetSelector = "UserSet2"
        cam_array[i].PixelFormat = "BayerRG8"
        cam_array[i].UserSetLoad.Execute()
        while cam_array[i].NumReadyBuffers.GetValue() > 0:
            cam_array[i].RetrieveResult(5000, py.TimeoutHandling_Return)
    # for cam in cam_array:
    #     if cam.DeviceInfo.GetUserDefinedName() == CameraIDs[0]:
    #         TriggerCam = cam
    #         cam.SetCameraContext(0)
    #     elif cam.DeviceInfo.GetUserDefinedName() == CameraIDs[1]:
    #         cam.SetCameraContext(1)
    #     elif cam.DeviceInfo.GetUserDefinedName() == CameraIDs[2]:
    #         cam.SetCameraContext(2)
    #     elif cam.DeviceInfo.GetUserDefinedName() == CameraIDs[3]:
    #         cam.SetCameraContext(3)
    #     elif cam.DeviceInfo.GetUserDefinedName() == CameraIDs[4]:
    #         cam.SetCameraContext(4)
    #     elif cam.DeviceInfo.GetUserDefinedName() == CameraIDs[5]:
    #         cam.SetCameraContext(5)
    #     cam.UserSetSelector = "UserSet2"
    #     cam.PixelFormat = "BayerRG8"
    #     cam.UserSetLoad.Execute()
    #     while cam.NumReadyBuffers.GetValue() > 0:
    #         cam.RetrieveResult(5000, py.TimeoutHandling_Return)
    cam_array.StartGrabbing(py.GrabStrategy_LatestImageOnly)
    ImagePublisher()

if __name__ == "__main__":
    StartCameras()
