#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32MultiArray
import numpy as np
import math
import pygame
import sched
import time
class ManualPublisher:

    def __init__(self):
        self.publisher_ = rospy.Publisher(
            'manual_control',
            Float32MultiArray,
            queue_size=1
        )
        self.max_speed = 1000.0
        self.timer_period = 0.05
        self.scheduler = sched.scheduler(time.time, time.sleep)
        self.scheduler.enter(self.timer_period, 1, self.joystick_callback)
        self.scheduler.run()

    def joystick_callback(self):
        msg = Float32MultiArray()

        pygame.init()
        pygame.joystick.init()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
        try:
            axis_x = float(-1*pygame.joystick.Joystick(0).get_axis(1))
            axis_y = float(-1*pygame.joystick.Joystick(0).get_axis(0))
        except:
            axis_x = 0.0
            axis_y = 0.0

        if axis_x > -0.09 and axis_x < 0.09:
            axis_x = 0.0
        if axis_y > -0.09 and axis_y < 0.09:
            axis_y = 0.0

        [r,theta] = self.get_angle(axis_x, axis_y)
        L_ratio = self.calc_left_ratio(theta)
        R_ratio = self.calc_right_ratio(theta)
        msg.data = self.calc_speed(L_ratio, R_ratio, r)

        self.publisher_.publish(msg)

        #self.get_logger().info("Publishing: %s" % str(msg.data))
        print(msg.data)
        self.scheduler.enter(self.timer_period, 1, self.joystick_callback)

    def calc_speed(self, left_ratio, right_ratio, magnitude):
        left_percentage = max(min(left_ratio * magnitude, 1), -1)
        right_percentage = max(min(right_ratio * magnitude, 1), -1)
        left_speed = self.max_speed * left_percentage
        right_speed = self.max_speed * right_percentage
        return [left_speed, right_speed]
    
    def get_angle(self, x, y):
        r = np.sqrt(x ** 2 + y ** 2)
        theta = math.degrees(math.atan2(x, y))
        return [r, theta]
    
    def calc_left_ratio(self, theta):
        if -180 <= theta < -90:
            ratio = -1
        elif -90 <= theta < 0:
            ratio = 1 + (2 * theta)/90
        elif 0 <= theta <= 90:
            ratio = 1
        elif 90 < theta <= 180:
            ratio = 1 - ((2*(theta - 90))/90)
        else: ratio = 0
        return ratio

    def calc_right_ratio(self, theta):
        if -180 <= theta < -90:
            ratio = 1 + (2 * (theta + 90))/90
        elif -90 <= theta <= 0:
            ratio = 1
        elif 0 < theta < 90:
            ratio = 1 - ((2*theta)/90)
        elif 90 <= theta <= 180:
            ratio = -1
        else: ratio = 0
        return ratio

def main(args=None):
    rospy.init_node('manual_publisher')
    
    ManualPublisher()

    rospy.spin()

    rospy.signal_shutdown('closing')

if __name__ == '__main__':
    main()

        
        
