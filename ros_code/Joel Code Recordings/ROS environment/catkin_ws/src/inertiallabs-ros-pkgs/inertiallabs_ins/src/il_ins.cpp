#include<iostream>
#include<unistd.h>
#include<math.h>
#include<stdlib.h>
#include <ros/ros.h>
#include <tf2/LinearMath/Quaternion.h>

//Inertial Labs source header
#include "ILDriver.h"

//adding message type headers
#include <inertiallabs_msgs/sensor_data.h>
#include <inertiallabs_msgs/ins_data.h>
#include <inertiallabs_msgs/gps_data.h>
#include <inertiallabs_msgs/gnss_data.h>
#include <inertiallabs_msgs/marine_data.h>
#include <sensor_msgs/Imu.h>
#include <sensor_msgs/NavSatFix.h>

//Publishers

struct Context {
	ros::Publisher publishers[7];
	std::string imu_frame_id;
};

void publish_device(IL::INSDataStruct *data, void* contextPtr)
{
	Context * context = reinterpret_cast<Context*>(contextPtr);
	static int seq=0;
	seq++;

	inertiallabs_msgs::sensor_data msg_sensor_data;
	inertiallabs_msgs::ins_data msg_ins_data;
	inertiallabs_msgs::gps_data msg_gps_data;
	inertiallabs_msgs::gnss_data msg_gnss_data;
	inertiallabs_msgs::marine_data msg_marine_data;
	sensor_msgs::Imu msg_imu_data;
	sensor_msgs::NavSatFix msg_nav_data;

	tf2::Quaternion myQuaternion;

	ros::Time timestamp = ros::Time::now();

	if (context->publishers[0].getNumSubscribers() > 0)
	{
		msg_sensor_data.header.seq = seq;
		msg_sensor_data.header.stamp = timestamp;
		msg_sensor_data.header.frame_id = context->imu_frame_id;
		msg_sensor_data.Mag.x = data->Mag[0];
		msg_sensor_data.Mag.y = data->Mag[0];
		msg_sensor_data.Mag.z = data->Mag[0];
		msg_sensor_data.Accel.x = data->Acc[0];
		msg_sensor_data.Accel.y = data->Acc[1];
		msg_sensor_data.Accel.z = data->Acc[2];
		msg_sensor_data.Gyro.x = data->Gyro[0];
		msg_sensor_data.Gyro.y = data->Gyro[1];
		msg_sensor_data.Gyro.z = data->Gyro[2];
		msg_sensor_data.Temp = data->Temp;
		msg_sensor_data.Vinp = data->VSup;
		msg_sensor_data.Pressure = data->hBar;
		msg_sensor_data.Barometric_Height = data->pBar;
		context->publishers[0].publish(msg_sensor_data);
	}

	if (context->publishers[1].getNumSubscribers() > 0)
	{
		msg_ins_data.header.seq = seq;
		msg_ins_data.header.stamp = timestamp;
		msg_ins_data.header.frame_id = context->imu_frame_id;
		msg_ins_data.YPR.x = data->Heading;
		msg_ins_data.YPR.y = data->Pitch;
		msg_ins_data.YPR.z = data->Roll;
		msg_ins_data.OriQuat.w = data->Quat[0];
		msg_ins_data.OriQuat.x = data->Quat[1];
		msg_ins_data.OriQuat.y = data->Quat[2];
		msg_ins_data.OriQuat.z = data->Quat[3];
		msg_ins_data.LLH.x = data->Latitude;
		msg_ins_data.LLH.y = data->Longitude;
		msg_ins_data.LLH.z = data->Altitude;
		msg_ins_data.Vel_ENU.x = data->VelENU[0];
		msg_ins_data.Vel_ENU.y = data->VelENU[1];
		msg_ins_data.Vel_ENU.z = data->VelENU[2];
		msg_ins_data.GPS_INS_Time = data->GPS_INS_Time;
		msg_ins_data.GPS_IMU_Time = data->GPS_IMU_Time;
		msg_ins_data.GPS_mSOW.data = data->ms_gps;
		msg_ins_data.Solution_Status.data = data->INSSolStatus;
        msg_ins_data.USW = data->USW;
		context->publishers[1].publish(msg_ins_data);
	}

	if (context->publishers[2].getNumSubscribers() > 0)
	{
		msg_gps_data.header.seq = seq;
		msg_gps_data.header.stamp = timestamp;
		msg_gps_data.header.frame_id = context->imu_frame_id;
		msg_gps_data.LLH.x = data->LatGNSS;
		msg_gps_data.LLH.y = data->LonGNSS;
		msg_gps_data.LLH.z = data->AltGNSS;
		msg_gps_data.HorSpeed = data->V_Hor;
		msg_gps_data.SpeedDir = data->Trk_gnd;
		msg_gps_data.VerSpeed = data->V_ver;
		context->publishers[2].publish(msg_gps_data);
	}

	if (context->publishers[3].getNumSubscribers() > 0)
	{
		msg_gnss_data.header.seq = seq;
		msg_gnss_data.header.stamp = timestamp;
		msg_gnss_data.header.frame_id = context->imu_frame_id;
		msg_gnss_data.GNSS_info_1 = data->GNSSInfo1;
		msg_gnss_data.GNSS_info_2 = data->GNSSInfo2;
		msg_gnss_data.Number_Sat = data->SVsol;
		msg_gnss_data.GNSS_Velocity_Latency = data->GNSSVelLatency;
		msg_gnss_data.GNSS_Angles_Position_Type = data->AnglesType;
		msg_gnss_data.GNSS_Heading = data->Heading_GNSS;
		msg_gnss_data.GNSS_Pitch = data->Pitch_GNSS;
		msg_gnss_data.GNSS_GDOP = data->GDOP;
		msg_gnss_data.GNSS_PDOP = data->PDOP;
		msg_gnss_data.GNSS_HDOP = data->HDOP;
		msg_gnss_data.GNSS_VDOP = data->VDOP;
		msg_gnss_data.GNSS_TDOP = data->TDOP;
		msg_gnss_data.New_GNSS_Flags = data->NewGPS;
		msg_gnss_data.Diff_Age = data->DiffAge;
		context->publishers[3].publish(msg_gnss_data);
	}

	if (context->publishers[4].getNumSubscribers() > 0)
	{
		msg_marine_data.header.seq = seq;
		msg_marine_data.header.stamp = timestamp;
		msg_marine_data.header.frame_id = context->imu_frame_id;
		msg_marine_data.Heave = data->Heave;
		msg_marine_data.Surge = data->Surge;
		msg_marine_data.Sway = data->Sway;
		msg_marine_data.Heave_velocity = data->Heave_velocity;
		msg_marine_data.Surge_velocity = data->Surge_velocity;
		msg_marine_data.Sway_velocity = data->Sway_velocity;
		msg_marine_data.Significant_wave_height = data->significant_wave_height;
		context->publishers[4].publish(msg_marine_data);
	}

	if (context->publishers[5].getNumSubscribers() > 0)
	{
		msg_imu_data.header.seq = seq;
		msg_imu_data.header.stamp = timestamp;
		msg_imu_data.header.frame_id = "base_link";
		msg_imu_data.linear_acceleration.x = (data->Acc[0]) * 9.80665;
		msg_imu_data.linear_acceleration.y = (data->Acc[1]) * 9.80665;
		msg_imu_data.linear_acceleration.z = (data->Acc[2]) * 9.80665;
		msg_imu_data.angular_velocity.x = (data->Gyro[0])*0.01745329251;
		msg_imu_data.angular_velocity.y = (data->Gyro[1])*0.01745329251;
		msg_imu_data.angular_velocity.z = (data->Gyro[2])*0.01745329251;
		myQuaternion.setRPY((data->Roll)*0.01745329251,(data->Pitch)*0.01745329251,(data->Heading)*0.01745329251);
		msg_imu_data.orientation.x = myQuaternion.getX();
		msg_imu_data.orientation.y = myQuaternion.getY();
		msg_imu_data.orientation.z = myQuaternion.getZ();
		msg_imu_data.orientation.w = myQuaternion.getW();
		msg_imu_data.orientation_covariance[0] = 0.01;
		msg_imu_data.orientation_covariance[4] = 0.01;
		msg_imu_data.orientation_covariance[8] = 0.01;
		msg_imu_data.angular_velocity_covariance[0] = 0.01;
		msg_imu_data.angular_velocity_covariance[4] = 0.01;
		msg_imu_data.angular_velocity_covariance[8] = 0.01;
		msg_imu_data.linear_acceleration_covariance[0] = 0.01;
		msg_imu_data.linear_acceleration_covariance[4] = 0.01;
		msg_imu_data.linear_acceleration_covariance[8] = 0.01;
		context->publishers[5].publish(msg_imu_data);
	}

	if (context->publishers[6].getNumSubscribers() > 0)
	{
		msg_nav_data.header.seq = seq;
		msg_nav_data.header.stamp = timestamp;
		msg_nav_data.header.frame_id = "base_link";
		msg_nav_data.latitude = data->Latitude;
		msg_nav_data.longitude = data->Longitude;
		msg_nav_data.altitude = data->Altitude;
		msg_nav_data.position_covariance[0] = 0.1;
		msg_nav_data.position_covariance[1] = 0;
		msg_nav_data.position_covariance[2] = 0;
		msg_nav_data.position_covariance[3] = 0;
		msg_nav_data.position_covariance[4] = 0.1;
		msg_nav_data.position_covariance[5] = 0;
		msg_nav_data.position_covariance[6] = 0;
		msg_nav_data.position_covariance[7] = 0;
		msg_nav_data.position_covariance[8] = 0.1;
		msg_nav_data.position_covariance_type = 0;
		msg_nav_data.status.status = 0;
		msg_nav_data.status.service = 3;
		context->publishers[6].publish(msg_nav_data);
	}
}

int main(int argc, char** argv)
{
	ros::init(argc, argv, "il_ins");
	ros::NodeHandle n;
	ros::NodeHandle np("~");
	ros::Rate r(100); // 100 hz
	std::string port;
	IL::Driver ins;
	int ins_output_format;
	std::string imu_frame_id;
	Context context;

	//command line varibales
	//usb-FTDI_FT230X_Basic_UART_DK0AA7VU-if00-port0
	//usb-FTDI_FT230X_Basic_UART_DK0ABF9H-if00-port0
	np.param<std::string>("ins_url", port, "serial:/dev/ttyS0:115200");
	np.param<int>("ins_output_format", ins_output_format, 0x58);

	//Initializing Publishers
	context.publishers[0] = np.advertise<inertiallabs_msgs::sensor_data>("/Inertial_Labs/sensor_data", 1);
	context.publishers[1] = np.advertise<inertiallabs_msgs::ins_data>("/Inertial_Labs/ins_data", 1);
	context.publishers[2] = np.advertise<inertiallabs_msgs::gps_data>("/Inertial_Labs/gps_data", 1);
	context.publishers[3] = np.advertise<inertiallabs_msgs::gnss_data>("/Inertial_Labs/gnss_data", 1);
	context.publishers[4] = np.advertise<inertiallabs_msgs::marine_data>("/Inertial_Labs/marine_data", 1);
	context.publishers[5] = np.advertise<sensor_msgs::Imu>("/imu_data", 1);
	context.publishers[6] = np.advertise<sensor_msgs::NavSatFix>("/gps", 1);

	ROS_INFO("connecting to INS at URL %s\n",port.c_str());

	auto il_err = ins.connect(port.c_str());
	if (il_err != 0)
	{
		ROS_FATAL("Could not connect to the INS on this URL %s\n",
				  port.c_str()
		);
		exit(EXIT_FAILURE);
	}

	if (ins.isStarted())
	{
		ins.stop();
	}
	auto devInfo = ins.getDeviceInfo();
	auto devParams = ins.getDeviceParams();
	std::string SN(reinterpret_cast<const char *>(devInfo.IDN), 8);
	ROS_INFO("Found INS S/N %s\n", SN.c_str());
	context.imu_frame_id = SN;
	il_err = ins.start(ins_output_format);
	if (il_err != 0)
	{
		ROS_FATAL("Could not start the INS: %i\n", il_err);
		ins.disconnect();
		exit(EXIT_FAILURE);
	}
	ins.setCallback(&publish_device, &context);
	ROS_INFO("publishing at %d Hz\n", devParams.dataRate);
	ROS_INFO("rostopic echo the topics to see the data");
	ros::spin();
	std::cout << "Stopping INS... " << std::flush;
	ins.stop();
	std::cout << "Disconnecting... " << std::flush;
	ins.disconnect();
	std::cout << "Done." << std::endl;
	return 0;
}
