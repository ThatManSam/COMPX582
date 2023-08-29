#!/usr/bin/python3

import rospy
from PIL import Image
from inertiallabs_msgs.msg import ins_data, sensor_data, gnss_data
from zsr.msg import ImageBundle, zsrMsg
import numpy as np
import os
import yaml
import json
from cv_bridge import CvBridge, CvBridgeError
import cv2
import time
import rosbag

FolderPath = "/media/externaldrive/ExtractedBags/SA3_2023-07-25-14-35-34_0/"
ROSBagPath = "/media/externaldrive/bags/SA3_2023-07-25-14-35-34_0.bag"

ConfigLocation = "/home/billy/CameraConfigs/"
bridge = CvBridge()

def GetConfigs():
    global CameraParams
    CameraParams = {}
    Configs = [Config for Config in os.listdir(ConfigLocation) if (Config[-5:] == '.yaml')]
    for Config in Configs:
        with open(ConfigLocation + Config, "r") as stream:
            calib = yaml.safe_load(stream)
        calibK = np.array(calib['camera_matrix']['data']).reshape((3,3))
        calibD = np.array(calib['distortion_coefficients']['data']).reshape((1,5))
        calibP = np.array(calib['projection_matrix']['data']).reshape((3,3))
        calibR = np.array(calib['rectification_matrix']['data']).reshape((3,3))
        calibMainBaseline = float(calib['maincambaseline'])
        calibWidth = calib['image_width']
        calibHeight = calib['image_height']
        AOVHorizontal = float(calib['AOVHorizontal'])
        AOVVertical = float(calib['AOVVertical'])
        MapX, MapY = cv2.initUndistortRectifyMap(calibK,calibD,calibR,calibP,(calibWidth,calibHeight),5)
        CameraParams[Config[:-5]] = {'Intrinsic': calibK, 'Distortion': calibD, 'Projection': calibP, 'MainCamBaseline': calibMainBaseline, 'ImageWidth': calibWidth, 'ImageHeight': calibHeight, 'AOVHorizontal': AOVHorizontal, 'AOVVertical': AOVVertical, 'MapX': MapX, 'MapY': MapY}
        
    for Camera in CameraParams:
        if Camera[-1] == "R":
            CameraParams[Camera]['Baseline'] = float(calibMainBaseline - CameraParams[Camera[:-1]+"L"]['MainCamBaseline'])

def ExtractIL(topic, JSONFileName):
    Messages = []
    for topic, msg, t in ROSBag.read_messages(topics=[topic]):
        YAMLMessage = yaml.load(str(msg))
        Messages.append(YAMLMessage)
    with open(FolderPath + JSONFileName, 'w') as JSONFile:
        json.dump(Messages, JSONFile, indent=4, separators=(',',': '))
    print("Extracted from " + topic)


def ProcessImages():
    StartTime = time.time()
    ImageNo = 0
    for topic, images, t in ROSBag.read_messages(topics=["/baslerimages"]):
        ImageNo += 1
        print("Processing Image " + str(ImageNo))

        Time = images.header.stamp.secs*10**9+images.header.stamp.nsecs

        #Save images to folder
        Images = images.Images
        Cameras = images.DeviceIDs
        CameraIDs = []
        for Camera in Cameras:
            CameraIDs.append(Camera.data)
        print(CameraIDs)
        for Device in range(0,len(Images)):
            CameraID = CameraIDs[Device]
            FileName = CameraID + "_" + str(Time) + ".jpg"
            RawImage = bridge.imgmsg_to_cv2(Images[Device], "rgb8")
            RawImage = cv2.remap(RawImage,CameraParams[CameraID]['MapX'],CameraParams[CameraID]['MapY'],cv2.INTER_LINEAR)
            RawImage = cv2.rotate(RawImage, cv2.ROTATE_180)
            ProcessedImage = Image.fromarray(RawImage)
            ProcessedImage.save(FolderPath + FileName)
            #Send processed image message
            if (CameraID[-1] == "L") and (CameraID[:-1] + "R" in CameraIDs):
                SecondaryCameraID = CameraID[:-1] + "R"
                SecondaryFileName = SecondaryCameraID + "_" + str(Time) + ".jpg"
            else:
                SecondaryCameraID = "None"
                SecondaryFileName = "None"

    print("Time to process: " + str(time.time() - StartTime))

def ProcessGPS():
    global FolderPath, INSJSONFile, ROSBag
    GetConfigs()
    ROSBag = rosbag.Bag(ROSBagPath, "r")
    ExtractIL("/Inertial_Labs/ins_data","INS.json")
    ExtractIL("/Inertial_Labs/sensor_data","Sensor.json")
    ProcessImages()

if __name__ == "__main__":
    ProcessGPS()