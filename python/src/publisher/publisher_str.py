#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def publisher_str():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('publisher_str', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher_str()
    except rospy.ROSInterruptException:
        pass
