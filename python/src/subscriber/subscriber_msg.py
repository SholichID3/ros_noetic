#!/usr/bin/env python3
import rospy
from python.msg import DataType

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "The number = ", msg.f6_value)
    rospy.loginfo(rospy.get_caller_id() + "The number = ", msg.f5_value)
    rospy.loginfo(rospy.get_caller_id() + "The number = ", msg.i6_value)
    rospy.loginfo(rospy.get_caller_id() + "The number = ", msg.i5_value)
    
def subscriber_msg():
    rospy.init_node('subscriber_msg', anonymous=True)
    rospy.Subscriber("chatter/msg", DataType, callback)
    rospy.spin()

if __name__ == '__main__':
    subscriber_msg()
