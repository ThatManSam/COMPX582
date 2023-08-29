#!/usr/bin/python3

import rospy
from PIL import Image
from inertiallabs_msgs.msg import ins_data, sensor_data, gnss_data
from zsr.msg import ImageBundle, zsrMsg
import numpy as np
import geopy
import geopy.distance
import math
import os
import yaml
from cv_bridge import CvBridge, CvBridgeError
import cv2
import csv
from rospy_message_converter import message_converter
from datetime import datetime
import time

FolderLocation = "/media/externaldrive/CompletedRuns/"
GPSLocations = []
bridge = CvBridge()

def ReceiveINS(data):
    time = data.header.stamp.secs*10**9+data.header.stamp.nsecs
    if len(GPSLocations) >= 100:
        del GPSLocations[0]
    GPSLocations.append([time,data.LLH.x,data.LLH.y,data.LLH.z,data.Vel_ENU.x,data.Vel_ENU.y,data.Vel_ENU.z])
    #RawMessage =  message_converter.convert_ros_message_to_dictionary(data)
    #INSMessageWriter.writerow([str(RawMessage)])

def ReceiveSensor(data):
    # time = data.header.stamp.secs*10**9+data.header.stamp.nsecs
    # if len(GPSLocations) >= 100:
    #     del GPSLocations[0]
    # GPSLocations.append([time,data.LLH.x,data.LLH.y,data.LLH.z,data.Vel_ENU.x,data.Vel_ENU.y,data.Vel_ENU.z])
    RawMessage =  message_converter.convert_ros_message_to_dictionary(data)
    SensorMessageWriter.writerow([str(RawMessage)])

def ReceiveGNSS(data):
    RawMessage =  message_converter.convert_ros_message_to_dictionary(data)
    GNSSMessageWriter.writerow([str(RawMessage)])

def ProcessImages(images):
    StartTime = time.time()
    #Get time images taken and find closest INS message
    Time = images.header.stamp.secs*10**9+images.header.stamp.nsecs
    ClosestGPSLocation = GPSLocations[np.argmin(abs(Time - np.array(GPSLocations)[:,0]))]

    #Calculate GPS location when images taken using GPS location, velocity and time elapsed since last GPS message.
    GPSPoint = geopy.Point(ClosestGPSLocation[1],ClosestGPSLocation[2])
    TimeDifference = (ClosestGPSLocation[0]-Time)*10**-9
    Velocity = math.sqrt(ClosestGPSLocation[4]**2+ClosestGPSLocation[5]**2)
    if (ClosestGPSLocation[4] > 0):
        if (ClosestGPSLocation[5] > 0): #If between 0 and 90 degrees
            Bearing = math.degrees(math.atan(ClosestGPSLocation[4]/ClosestGPSLocation[5]))
        elif (ClosestGPSLocation[5] < 0): #If between 90 and 180 degrees
            Bearing = 180 + math.degrees(math.atan(ClosestGPSLocation[4]/ClosestGPSLocation[5]))
        else:
            Bearing = 90
    elif (ClosestGPSLocation[4] < 0):
        if (ClosestGPSLocation[5] > 0): #If between 270 and 360 degrees
            Bearing = 360 + math.degrees(math.atan(ClosestGPSLocation[4]/ClosestGPSLocation[5]))
        elif (ClosestGPSLocation[5] < 0): #If between 180 and 270 degrees
            Bearing = 180 + math.degrees(math.atan(ClosestGPSLocation[4]/ClosestGPSLocation[5]))
        else:
            Bearing = 270
    else:
        if ClosestGPSLocation[5] < 0: #If travelling south
            Bearing = 180
        else: #If travelling north or stationary
            Bearing = 0
    Distance = Velocity*abs(TimeDifference)
    #If GPS location is newer images were taken in opposite direction to bearing
    if TimeDifference >= 0:
        Bearing = -Bearing
    ImagePoint = geopy.distance.geodesic(meters=Distance).destination(GPSPoint, Bearing)
    ImagePointDD = [ImagePoint.latitude, ImagePoint.longitude]

    #Construct zsrMsg
    msg = zsrMsg()
    msg.latitude = ImagePointDD[0]
    msg.longitude = ImagePointDD[1]
    msg.altitude = ClosestGPSLocation[3]
    msg.heading = Bearing
    msg.feature.data = "flowerBuds"
    msg.measure = 0
    msg.process.data = "baslerStereoDetectron"
    msg.propertyType.data = "flowerBuds/m^2"
    msg.resultQuality.data = "Unprocessed"
    msg.utcTime = Time
    msg.OrchardID.data = FolderName
    msg.INSlatitude = ClosestGPSLocation[1]
    msg.INSlongitude = ClosestGPSLocation[2]
    msg.INSaltitude = ClosestGPSLocation[3]
    msg.INStime = ClosestGPSLocation[0]

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
        ProcessedImage = Image.fromarray(RawImage)
        ProcessedImage.save(FolderPath + FileName)
        #Send processed image message
        if (CameraID[-1] == "L") and (CameraID[:-1] + "R" in CameraIDs):
            SecondaryCameraID = CameraID[:-1] + "R"
            SecondaryFileName = SecondaryCameraID + "_" + str(Time) + ".jpg"
        else:
            SecondaryCameraID = "None"
            SecondaryFileName = "None"
        msg.parameter.data = FolderName + "." +CameraID
        msg.CameraID.data = CameraID
        msg.SecondaryCameraID.data = SecondaryCameraID
        msg.ImageID.data = FileName
        msg.SecondaryImageID.data = SecondaryFileName
        pub.publish(msg)
    print("Time to process: " + str(time.time() - StartTime))

def ProcessGPS():
    global FolderPath, FolderName, pub, INSMessageWriter, SensorMessageWriter, GNSSMessageWriter
    rospy.init_node('talker', anonymous=True)
    FolderName = str(rospy.get_param("~OrchardID")).replace("\n","")
    FolderPath = (str(rospy.get_param("~FolderLocation")) + FolderName + "/").replace('\n', '')
    os.mkdir(FolderPath)
    #INSMessageFile = open(FolderPath + 'INSMessages.csv', 'a')
    #INSMessageWriter = csv.writer(INSMessageFile,delimiter=',')
    #SensorMessageFile = open(FolderPath + 'SensorMessages.csv', 'a')
    #SensorMessageWriter = csv.writer(SensorMessageFile,delimiter=',')
    #GNSSMessageFile = open(FolderPath + 'GNSSMessages.csv', 'a')
    #GNSSMessageWriter = csv.writer(GNSSMessageFile,delimiter=',')
    rospy.Subscriber("/Inertial_Labs/ins_data", ins_data, ReceiveINS)
    #rospy.Subscriber("/Inertial_Labs/sensor_data", sensor_data, ReceiveSensor)
    #rospy.Subscriber("/Inertial_Labs/gnss_data", gnss_data, ReceiveGNSS)
    rospy.Subscriber("/baslerimages", ImageBundle, ProcessImages)
    pub = rospy.Publisher('/zsrMsg', zsrMsg, queue_size=10)
    rospy.spin()
    #INSMessageFile.close()
    #SensorMessageFile.close()

if __name__ == "__main__":
    ProcessGPS()