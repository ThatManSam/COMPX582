#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray
import serial
import subprocess
import time
import re
import openpyxl

class MotorControlSubscriber(Node):

    def __init__(self):
        super().__init__('motor_control_subscriber')
        self.main_subscription = self.create_subscription(
            Float32MultiArray,
            'dist_transfer',
            self.main_callback,
            1)
        self.main_subscription

        self.autonomous_subscription = self.create_subscription(
            Float32MultiArray,
            'auto_control',
            self.autonomous_callback,
            1)
        self.autonomous_subscription

        self.manual_subscription = self.create_subscription(
            Float32MultiArray,
            'manual_control',
            self.manual_callback,
            1)
        self.manual_subscription

        self.auto_speed = []
        self.manual_speed = []
        self.ser = serial.Serial(port='/dev/serial/by-id/usb-Prolific_Technology_Inc._USB-Serial_Controller_AUCWb11BS14-if00-port0', baudrate=115200, bytesize=8, stopbits=serial.STOPBITS_ONE, parity=serial.PARITY_NONE)
        self.ser2 = serial.Serial(port='/dev/serial/by-id/usb-Prolific_Technology_Inc._USB-Serial_Controller_CYABb11BS14-if00-port0', baudrate=115200, bytesize=8, stopbits=serial.STOPBITS_ONE, parity=serial.PARITY_NONE)
        self.flag = 1
        # self.motor1_voltage = ''
        # self.motor1_battery_amps = ''
        # self.motor1_motor_amps = ''
        # self.motor1_code = 0
        # self.motor2_voltage = ''
        # self.motor2_battery_amps = ''
        # self.motor2_motor_amps = ''
        # self.motor2_code = 0
        self.max_ratio = 1023
        self.read_list = []
        self.read2_list = []

        self.folder_path = "/home/jetson/autonomous_tractor_data/"
        self.file_name = "battery_data.xlsx"
        self.file = self.folder_path + self.file_name

        self.workbook = openpyxl.Workbook()
        self.workbook.save(self.file)


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
                self.ser.flushInput()
                self.ser2.flushInput()


                # max speed is 1000 which is 1500rpm 
                # this piece controls the speed
                command = '!M {}\r'.format(-1*motor_speed[0])
                command2 = '!M {}\r'.format(motor_speed[1])
                self.ser.write(command.encode('ascii'))
                self.ser2.write(command2.encode('ascii'))

                # volts_command = '?V\r'
                # self.ser.write(volts_command.encode('ascii'))
                # self.ser2.write(volts_command.encode('ascii'))

                motor_amps_command = '?A\r'
                self.ser.write(motor_amps_command.encode('ascii'))
                self.ser2.write(motor_amps_command.encode('ascii'))

                # batt_amps_command = '?BA\r'
                # self.ser.write(batt_amps_command.encode('ascii'))
                # self.ser2.write(batt_amps_command.encode('ascii'))

                # read = self.ser.read().decode()
                # read2 = self.ser2.read().decode()

                # if len(self.read_list) != 0:   
                #     if read == self.read_list[0]:
                #         print(self.read_list)
                #         self.read_list = []
                #         self.ser.flushInput()

                count1 = 0
                while count1 < 4:
                    read = self.ser.read().decode()
                    self.read_list.append(read)
                    if read == '\r':
                        count1 += 1
                        print(count1)

                count2 = 0
                while count2 < 4:
                    read2 = self.ser2.read().decode()
                    self.read2_list.append(read2)
                    if read2 == '\r':
                        count2 += 1
                        print(count2)
                
                print(self.read_list)
                print(self.read2_list)
                self.read_list = []
                self.read2_list = []


                    

                # if read == 'V':
                #     self.motor1_code = 1
                # elif read == 'A' and self.motor1_code != 3:
                #     self.motor1_code = 2
                # elif read == 'B':
                #     self.motor1_code = 3
                # elif read == '!':
                #     self.motor1_code = 0

                # if read2 == 'V':
                #     self.motor2_code = 1
                # elif read2 == 'A' and self.motor2_code != 3:
                #     self.motor2_code = 2
                # elif read2 == 'B':
                #     self.motor2_code = 3
                # elif read2 == '!':
                #     self.motor2_code = 0

                # if self.motor1_code == 1:
                #     self.motor1_voltage += read
                # elif self.motor1_code == 2:
                #     self.motor1_motor_amps += read
                # elif self.motor1_code == 3:
                #     # if read == '\r':
                #     #     self.ser.flushInput()
                #     self.motor1_battery_amps += read

                # if self.motor2_code == 1:
                #     self.motor2_voltage += read2
                # elif self.motor2_code == 2:
                #     self.motor2_motor_amps += read2
                # elif self.motor2_code == 3:
                #     # if read2 == '\r':
                #     #     self.ser2.flushInput()
                #     self.motor2_battery_amps += read2

                # try:
                #     internal_volt = (float(self.motor1_voltage[4:7]))/10
                #     battery_volt = (float(self.motor1_voltage[12:16]))/100

                #     motor1_volt = (float(self.motor1_voltage[8:11]))/10
                #     motor1_motor_amp_match = re.search(r'\d+', self.motor1_motor_amps)
                #     motor1_motor_amp = float(motor1_motor_amp_match.group())
                #     motor1_batt_amp_match = re.search(r'\d+', self.motor1_battery_amps)
                #     motor1_batt_amp = float(motor1_batt_amp_match.group())

                #     motor2_volt = (float(self.motor2_voltage[8:11]))/10
                #     # motor2_motor_amp = self.motor2_motor_amps[0:2]
                #     motor2_motor_amp_match = re.search(r'\d+', self.motor2_motor_amps)
                #     motor2_motor_amp = float(motor2_motor_amp_match.group())
                #     motor2_batt_amp_match = re.search(r'\d+', self.motor2_battery_amps)
                #     motor2_batt_amp = float(motor2_batt_amp_match.group())
                #     # self.ser.flushInput()
                #     # self.ser2.flushInput()
                #     # self.ser.flushOuput()
                #     # self.ser2.flushOuput()

                # except:
                #     internal_volt = 0.0
                #     battery_volt = 0.0

                #     motor1_volt = 0.0
                #     motor1_motor_amp = 2.0
                #     motor1_batt_amp = 2.0
                    
                #     motor2_volt = 0.0
                #     motor2_motor_amp = 2.0
                #     motor2_batt_amp = 2.0
                    

                # print(internal_volt, battery_volt, motor1_volt, motor1_motor_amp, motor1_batt_amp, motor2_volt, motor2_motor_amp, motor2_batt_amp)

                # data = [internal_volt, battery_volt, motor1_volt, motor1_motor_amp, motor1_batt_amp, motor2_volt, motor2_motor_amp, motor2_batt_amp]

                # workbook = openpyxl.load_workbook(self.file)
                # sheet = workbook.active
                # sheet.append(data)
                # workbook.save(self.file)
                # workbook.close

def main(args=None):
    rclpy.init(args=args)

    motor_control_subscriber = MotorControlSubscriber()

    rclpy.spin(motor_control_subscriber)

    rclpy.shutdown()


if __name__ == '__main__':
    main()