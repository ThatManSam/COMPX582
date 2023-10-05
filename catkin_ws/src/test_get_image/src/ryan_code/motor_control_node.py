#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32MultiArray
import serial
import subprocess
import time

class MotorControlSubscriber:

    def __init__(self):
        self.main_subscription = rospy.Subscriber(
            'dist_transfer',
            Float32MultiArray,
            self.main_callback,
            queue_size=1
        )
        
        self.autonomous_subscription = rospy.Subscriber(
            'auto_control',
            Float32MultiArray,
            self.autonomous_callback,
            queue_size=1
        )
        
        self.manual_subscription = rospy.Subscriber(
            'manual_control',
            Float32MultiArray,
            self.manual_callback,
            queue_size=1
        )

        self.auto_speed = []
        self.manual_speed = []
        self.ser = serial.Serial(port='/dev/serial/by-id/usb-Prolific_Technology_Inc._USB-Serial_Controller_AUCWb11BS14-if00-port0', baudrate=115200, bytesize=8, stopbits=serial.STOPBITS_ONE, parity=serial.PARITY_NONE)
        self.ser2 = serial.Serial(port='/dev/serial/by-id/usb-Prolific_Technology_Inc._USB-Serial_Controller_CYABb11BS14-if00-port0', baudrate=115200, bytesize=8, stopbits=serial.STOPBITS_ONE, parity=serial.PARITY_NONE)
        self.flag = 1
        self.max_ratio = 1023

    def reset_usb(self):
        try:
            command = 'uhubctl -l 1-1.3 -a off'
            result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            time.sleep(2)
            command = 'uhubctl -l 1-1.3 -a on'
            result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if result.returncode == 0:
                print("usb reset correctly")
            else:
                print("usb reset failed")

            set_time = time.time()
            for i in range(100000000):
                i += 1

            time_taken = time.time() - set_time
            print(time_taken)
        
        except Exception as e:
            print(f"An error occured: {e}")

    def autonomous_callback(self, msg):
        self.auto_speed = msg.data

    def manual_callback(self, msg):
        self.manual_speed = msg.data
        
    def navigation_callback(self, msg):
        self.navigation_speed = msg.data

    def main_callback(self, msg):
        mode = int(msg.data[3])
        picking_ratio = (msg.data[2]/self.max_ratio)
        # print(picking_ratio)

        if mode == 0:
            if len(self.auto_speed) == 2:
                left_speed = self.auto_speed[0] * picking_ratio
                right_speed = self.auto_speed[1] * picking_ratio
                motor_speed = [left_speed, right_speed]
            else:
                motor_speed = [0, 0]
        else:
            motor_speed = self.manual_speed

        if len(motor_speed) == 2:
            emergency = int(msg.data[4])

            if emergency:
                self.flag = 1

            if not emergency and self.flag:
                self.flag = 0
                self.ser.close()
                self.ser2.close()
                self.reset_usb()
                self.ser.open()
                self.ser2.open()
                

            #print(emergency)
            if not emergency and not self.flag:
                #print(motor_speed)
                # self.ser.flushInput()
                # self.ser2.flushInput()


                # max speed is 1000 which is 1500rpm 
                # this piece controls the speed
                command = '!M {}\r'.format(-1*motor_speed[0])
                command2 = '!M {}\r'.format(motor_speed[1])
                self.ser.write(command.encode('ascii'))
                self.ser2.write(command2.encode('ascii'))

                volts_command = '?V\r'
                self.ser.write(volts_command.encode('ascii'))
                self.ser2.write(volts_command.encode('ascii'))

                motor_amps_command = '?A\r'
                self.ser.write(motor_amps_command.encode('ascii'))
                self.ser2.write(motor_amps_command.encode('ascii'))

                batt_amps_command = '?BA\r'
                self.ser.write(batt_amps_command.encode('ascii'))
                self.ser2.write(batt_amps_command.encode('ascii'))

                read = self.ser.read().decode()
                read2 = self.ser2.read().decode()

                print(read, read2)


def main(args=None):
    rospy.init_node("motor_controller")

    MotorControlSubscriber()

    rospy.spin()

    rospy.signal_shutdown("Closing")


if __name__ == '__main__':
    main()