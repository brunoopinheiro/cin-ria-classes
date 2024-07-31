#! /usr/bin/python3

import rospy
from nav_msgs.msg import Odometry


# Definition of the class
class MySub:

    def __init__(self) -> None:
        # Define the subscriber
        self.sub = rospy.Subscriber(
            '/mobile_base_controller/odom',
            Odometry,
            self.callback,
            queue_size=1,
        )

    # Definition of the callback function
    def callback(self, msg: Odometry):
        # self.counterValue = msg.data
        print(msg.pose)


if __name__ == '__main__':
    # Define the node
    rospy.init_node('TIAGo_odem_node')
    # Create an object of class MySub and run the init function
    sub_obj = MySub()
    # While ROS is running
    rospy.spin()
