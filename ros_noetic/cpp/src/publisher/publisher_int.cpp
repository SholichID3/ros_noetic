#include "ros/ros.h"
#include "std_msgs/Int64.h"

int main(int argc, char **argv)
{
  ros::init(argc, argv, "publisher_int");
  ros::NodeHandle n;

  ros::Publisher chatter_pub = n.advertise<std_msgs::Int64>("chatter/int", 1000);

  ros::Rate loop_rate(10);
 
  while (ros::ok())
  {
    std_msgs::Int64 msg;
    msg.data = 10;

    ROS_INFO("%i", msg.data);

    chatter_pub.publish(msg);

    ros::spinOnce();

    loop_rate.sleep();
  }
  
  return 0;
}
