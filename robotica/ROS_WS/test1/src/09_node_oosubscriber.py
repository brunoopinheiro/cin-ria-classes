#! /usr/bin/bash

import rospy
from std_msgs.msg import Int32


class MySub:

    def __init__(self) -> None:
        # Define the subscriber
        self.sub = rospy.Subscriber(
            'name',
            Int32,
            self.callback,
            queue_size=1,
        )
        # Message variables
        self.counter_value = 0

    # Definition of the function called by the subscriber
    def callback(self, msg):
        self.counter_value = msg.data

    def print_msg(self):
        print(self.counter_value)
