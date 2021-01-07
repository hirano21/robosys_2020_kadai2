#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32



def ss(message):
    rospy.loginfo(message.data)
    if message.data%3==0:
        print('nasu')
    if message.data%15==0:
        print('nasubi')

if __name__=='__main__':
    rospy.init_node('nasu')
    sub = rospy.Subscriber('count_up',Int32, ss)
    rospy.spin()
