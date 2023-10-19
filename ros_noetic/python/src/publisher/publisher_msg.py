#!/usr/bin/env python3

import rospy
from python.msg import DataType

def publisher_msg():
    pub = rospy.Publisher('chatter/msg', DataType, queue_size=10)
    rospy.init_node('publisher_msg', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        msg.f6_value = 10.15212511;
        msg.f5_value = 10.1351;
        msg.i6_value = 10000;
        msg.i5_value = 10;
        rospy.loginfo(msg.f6_value)
        rospy.loginfo(msg.f5_value)
        rospy.loginfo(msg.i6_value)
        rospy.loginfo(msg.i5_value)
        pub.publish(msg)
        rate.sleep()
      
if __name__ == '__main__':
    try:
        publisher_msg()
    except rospy.ROSInterruptException:
        pass
