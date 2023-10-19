#include "ros/ros.h"
#include "cpp/DataType.h"

void chatterRandomCallback(const cpp::DataType::ConstPtr& msg)
{
  ROS_INFO("The float64 value = ", msg->f6_value);
  ROS_INFO("The float32 value = ", msg->f5_value);
  ROS_INFO("The int64 value = ", msg->i6_value);
  ROS_INFO("The int32 value = ", msg->i5_value);
}

int main(int argc, char **argv)
{
 
  ros::init(argc, argv, "subscriber_msg");

  ros::NodeHandle n;

  ros::Subscriber sub = n.subscribe("chatter/datatype", 1000, chatterRandomCallback);

  ros::spin();

  return 0;
}
