#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray
import serial
import time

class UltrasonicPublisher(Node):

    def __init__(self, ser):
        super().__init__('ultrasonic_publisher')
        self.publisher_ = self.create_publisher(Float32MultiArray, 'dist_transfer', 1)
        timer_period = 0.05
        self.timer = self.create_timer(timer_period, self.dist_callback)
        self.ser = ser

    def calc_dist(self):
        try:
            self.ser.flushInput()

            # read the data from arduino over the serial
            line = self.ser.readline().decode().strip()
            data = line.split(",")
            
            left_dist = float(data[0])
            right_dist = float(data[1])
            speed = float(data[2])
            switch = float(data[3])
            emergency = float(data[4])

            return [left_dist, right_dist, speed, switch, emergency]
        
        except serial.SerialException:

            return [0.0, 0.0, 0.0, 1.0, 0.0]

    def dist_callback(self):
        msg = Float32MultiArray()
        msg.data = self.calc_dist()

        self.publisher_.publish(msg)
        print(msg.data)
        #self.get_logger().info("Publishing: %s" % str(msg.data))
        # time.sleep(0.05)

def main(args=None):
    ser = serial.Serial('/dev/serial/by-id/usb-Arduino__www.arduino.cc__0042_7513030383535170D0B2-if00', 115200)

    rclpy.init(args=args)

    ultrasonic_publisher = UltrasonicPublisher(ser)

    # ultrasonic_publisher.dist_callback()

    rclpy.spin(ultrasonic_publisher)

    ultrasonic_publisher.destroy_node()
    rclpy.shutdown

if __name__ == '__main__':
    main()