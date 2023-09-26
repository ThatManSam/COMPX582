#!/usr/bin/env python3

from math import sqrt
from typing import Optional, Tuple
from blessed import Terminal

import rospy

from geometry_msgs.msg import Twist

max_x = 0
max_z = 0

def ProcessTwist(twist: Twist, args: Tuple[Optional[Terminal]]=(None,)):
    global max_x, max_z
    term = args[0]
    if term is None:
        print("Can't show stats, no display")
        return
    
    max_x = max(max_x, abs(twist.linear.x))
    max_z = max(max_z, abs(twist.angular.z))
    
    with term.location(0, term.height // 2 - 5):
        term.clear()
        print(str(twist))
        print(f"Max X: {max_x}")
        print(f"Max Z: {max_z}")
        
def run_ros():
    rospy.init_node("test_get_twist", disable_signals=True)

    print("Ready")

    term = Terminal()
    with term.fullscreen(), term.cbreak():
        rospy.Subscriber("/cmd_vel", Twist, ProcessTwist, (term,))
        rospy.spin()
    print("Closing")
    rospy.signal_shutdown("Closing")

if __name__ == '__main__':
    run_ros()