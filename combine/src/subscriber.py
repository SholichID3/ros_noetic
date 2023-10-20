#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + " I heard %s", data.data)
    
def subscriber_str():
    rospy.init_node('subscriber', anonymous=True)
    rospy.Subscriber("combine", String, callback)
    rospy.spin()

if __name__ == '__main__':
    subscriber_str()
