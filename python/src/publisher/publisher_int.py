#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

def publisher_int():
    pub = rospy.Publisher('chatter/int', Int32, queue_size=10)
    rospy.init_node('publisher_int', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        hello_int = 10
        rospy.loginfo(hello_int)
        pub.publish(hello_int)
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher_int()
    except rospy.ROSInterruptException:
        pass
