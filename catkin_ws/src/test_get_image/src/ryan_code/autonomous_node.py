#!/usr/bin/env python3

import rospy

from std_msgs.msg import Float32MultiArray

class AutonomousSubscriber:

    def __init__(self):
        self.publisher_ = rospy.Publisher(
            'auto_control',
            Float32MultiArray,
            queue_size=1
        )
        
        self.subscription = rospy.Subscriber(
            'navigation_controller',
            Float32MultiArray,
            self.autonomous_callback,
            queue_size=1
        )

        self.Kp = 1
        self.Ki = 0
        self.Kd = 0
        self.setpoint = 0
        self.prev_error = 0
        self.integral = 0
        self.max_speed = 1000

    def PID_controller(self, measured_value):
        error = measured_value - self.setpoint

        p_term = self.Kp * error

        self.integral += error 
        i_term = self.Ki * self.integral

        d_term = self.Kd * (error - self.prev_error)

        control = p_term + i_term + d_term
        self.prev_error = error
        
        return control

    def autonomous_callback(self, data):
        # distance = data.data
        # right_dist = distance[0]
        # left_dist = distance[1]

        # right_measure = self.PID_controller(right_dist)
        # left_measure = self.PID_controller(left_dist)

        # if right_measure == 0 or left_measure == 0:
        #     left_ratio = 0
        #     right_ratio = 0
        # elif right_dist > 700 or left_dist > 700:
        #     left_ratio = 0
        #     right_ratio = 0
        # else:
        #     left_ratio = right_measure / left_measure
        #     right_ratio = left_measure / right_measure

        # left_speed = min(self.max_speed*left_ratio, self.max_speed)
        # right_speed = min(self.max_speed*right_ratio, self.max_speed)

        # msg = Float32MultiArray()

        # msg.data = [float(left_speed), float(right_speed)]

        # self.publisher_.publish(msg)
        print("#### NAV RECEIVED ####")
        print(data.data)
        self.publisher_.publish(data)

        # if int(data.data[3]) == 0:
            #self.get_logger().info("Publishing: %s" % str(msg.data))

def main(args=None):
    rospy.init_node('autonomous_publisher')
    AutonomousSubscriber()

    rospy.spin()

    rospy.signal_shutdown('closing')

if __name__ == '__main__':
    main()