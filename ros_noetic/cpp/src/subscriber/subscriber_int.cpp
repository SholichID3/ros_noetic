#include "ros/ros.h"
#include "std_msgs/Int64.h"

void chatterIntCallback(const std_msgs::Int64::ConstPtr& msg)
{
  ROS_INFO("The number : [%i]", msg->data);
}

int main(int argc, char **argv)
{
 
  ros::init(argc, argv, "subscriber_int");

  ros::NodeHandle n;

  ros::Subscriber sub = n.subscribe("chatter/int", 1000, chatterIntCallback);

  ros::spin();

  return 0;
}
