#! /usr/bin/python3

import rospy
from geometry_msgs.msg import Twist


rospy.init_node('publisher_tiago')

pub = rospy.Publisher('/mobile_base_controller/cmd_vel', Twist, queue_size=1)

rate = rospy.Rate(2)

variable = Twist()

count = 0
while not rospy.is_shutdown():

    if count % 2 == 0:
        variable.linear.x = 0.5
        variable.linear.y = 0.0
        variable.linear.z = 0.0
        variable.angular.x = 0.0
        variable.angular.y = 0.0
        variable.angular.z = 0.0
    else:
        variable.linear.x = 0.0
        variable.linear.y = 0.0
        variable.linear.z = 0.0
        variable.angular.x = 0.0
        variable.angular.y = 0.0
        variable.angular.z = 0.2

    pub.publish(variable)

    count += 1
    rate.sleep()
