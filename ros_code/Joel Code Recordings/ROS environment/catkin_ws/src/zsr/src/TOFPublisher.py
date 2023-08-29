#!/usr/bin/python3

import chronoptics.tof as tof
import numpy as np
import rospy
from std_msgs.msg import UInt32MultiArray

# Frame types to capture
types = [tof.FrameType.Z]

# Serial of camera to connect to, if empty will connect to the first found
serial = "2020021"

rospy.init_node('TOFPublisher', anonymous=True)
pub = rospy.Publisher('/TOFPublisher', UInt32MultiArray, queue_size=10)
msg = UInt32MultiArray()

while True:
    try:
        cam = tof.KeaCamera(tof.ProcessingConfig(), serial)
        cam.setOnCameraProcessing(True)

        cam_config = cam.getCameraConfig()
        cam_config.setDac([750,0,750,100])
        cam_config.setMlxMipiSpeed(960)
        cam_config.setModulationFrequency(0,10.0)
        cam_config.setDutyCycle(0,0.49)
        cam_config.setFrameTime(0,0)
        cam_config.setBinning(0,1)
        cam_config.setPhaseShifts(0,[0.0,0.25,0.5,0.75])
        cam_config.setIntegrationTime(0,[250,250,250,250])

        config = cam_config.defaultProcessing()
        config.setDistThresholdEnabled(True)
        config.setDistThresholdMin(100)
        config.setDistThresholdMax(1000)
        config.setAverageEnabled(True)
        config.setAverageNframes(5)

        cam.setProcessConfig(config)
        cam.setCameraConfig(cam_config)

        tof.selectStreams(cam, types)

        cam.start()

        # Capture frames
        while True:
            frames = cam.getFrames()
            ZValues = np.array(frames[0]).astype(int)
            msg.data = ZValues.flatten().tolist()
            pub.publish(msg)
            #ValidZValues = ZValues[ZValues > 0]
            #MeanHeight = np.mean(ValidZValues)
            #print(MeanHeight)
            del frames
    except:
        print("Error occured or could not connect to TOF camera")