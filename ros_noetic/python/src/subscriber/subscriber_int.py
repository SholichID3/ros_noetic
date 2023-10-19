#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "The number = %i ", data.data)
    
def subscriber_int():
    rospy.init_node('subscriber_int', anonymous=True)
    rospy.Subscriber("chatter/int", Int32, callback)
    rospy.spin()

if __name__ == '__main__':
    subscriber_int()
