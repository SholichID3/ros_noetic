#include "ros/ros.h"
#include "cpp/DataType.h"

int main(int argc, char **argv)
{
  ros::init(argc, argv, "publisher_msg");
  ros::NodeHandle n;

  ros::Publisher chatter_pub = n.advertise<cpp::DataType>("chatter/datatype", 1000);

  ros::Rate loop_rate(10);
 
  while (ros::ok())
  {
    cpp::DataType msg;

    msg.f6_value = 10.15212511;
    msg.f5_value = 10.1351;
    msg.i6_value = 10000;
    msg.i5_value = 10;

    ROS_INFO("float64 = %f", msg.f6_value);
    ROS_INFO("float32 = %f", msg.f5_value);
    ROS_INFO("int64 = %i", msg.f6_value);
    ROS_INFO("int32 = %i", msg.f6_value);

    chatter_pub.publish(msg);

    ros::spinOnce();

    loop_rate.sleep();
  }
  
  return 0;
}
