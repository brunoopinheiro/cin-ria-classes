#! /usr/bin/python3

import rospy
from turtlesim.msg import Pose


class TurtleSub:

    def __init__(self) -> None:
        self.sub = rospy.Subscriber(
            '/turtle1/pose',
            Pose,
            self.get_pose,
            queue_size=1,
        )
        self.pose_value = {
            'x': 0.0,
            'y': 0.0,
            'theta': 0.0,
        }

    def get_pose(self, pose: Pose) -> None:
        self.pose_value['x'] = pose.x
        self.pose_value['y'] = pose.y
        self.pose_value['theta'] = pose.theta

    def read_pose(self) -> None:
        print(self.pose_value)


if __name__ == "__main__":
    turtlesub = TurtleSub()
    rospy.init_node('turtle_subscriber')
    while not rospy.is_shutdown():
        turtlesub.read_pose()
