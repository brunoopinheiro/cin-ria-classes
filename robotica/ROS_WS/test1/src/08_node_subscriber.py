#! /usr/bin/python3

import time
import rospy
from std_msgs.msg import Int32


# define the function called by the subscriber
def callback(msg):
    print(msg.data)
    time.sleep(1)


rospy.init_node('simple_subscriber')


# Define the new subscriber
rospy.Subscriber('counter', Int32, callback, queue_size=1)

# Equivalent to an infinite while to not close the program
rospy.spin()
