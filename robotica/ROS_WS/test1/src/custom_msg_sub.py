#! /usr/bin/python3

import rospy
from test1.msg import Complex


def callback(msg):
    print(f'Read: {msg.real}')
    print(f'Imaginary: {msg.imaginary}')


rospy.init_node('custom_msg_subscriber')
sub = rospy.Subscriber('complex', Complex, callback)
rospy.spin()
