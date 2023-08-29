#!/usr/bin/env python
from __future__ import division
import rospy
#from sensor_msgs.msg import NavSatFix
#from geometry_msgs.msg import TwistWithCovarianceStamped
from std_msgs.msg import String
from zsr.msg import zsrMsg

import sys
feature = "flowerBuds"
process = "baslerStereoDetectron"
parameter = "null"
resultQuality = "null"
propertyType = "flowerBuds/m^2"

def talker():
    pub = rospy.Publisher('/zsrMsg', zsrMsg, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    msg = zsrMsg()
    msg.utcTime = 1645144260
    msg.latitude = -37.838753
    msg.longitude = 176.285090
    msg.altitude = 235.885000
    msg.propertyType.data = propertyType
    msg.measure = 70
    msg.feature.data = feature
    msg.process.data = process
    msg.parameter.data = parameter
    msg.resultQuality.data = resultQuality
    pub.publish(msg)


    while not rospy.is_shutdown():
        rospy.loginfo(msg)
        pub.publish(msg)
        rate.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
