#! /usr/bin/python3

import rospy
from geometry_msgs.msg import Twist


class TurtlePublisher:

    @property
    def rate(self) -> rospy.Rate:
        return self.__rate

    def __init__(self) -> None:
        self.pub = rospy.Publisher(
            '/turtle1/cmd_vel',
            Twist,
            queue_size=1,
        )
        self.__rate = rospy.Rate(2)
        self.__pubvalue = Twist()
        self.__pubvalue.linear.x = 0.0
        self.__pubvalue.linear.y = 0.0
        self.__pubvalue.linear.z = 0.0
        self.__pubvalue.angular.x = 0.0
        self.__pubvalue.angular.y = 0.0
        self.__pubvalue.angular.z = 0.0

    def publish(
            self,
            x: float,
            y: float,
            theta: float,
    ) -> None:
        self.__pubvalue.linear.x = x
        self.__pubvalue.linear.y = y
        self.__pubvalue.angular.z = theta
        self.pub.publish(
            self.__pubvalue,
        )
