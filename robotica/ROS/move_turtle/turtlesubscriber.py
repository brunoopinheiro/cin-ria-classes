#! /usr/bin/python3

import rospy
from turtlesim.msg import Pose
from typing import Dict


class TurtleSub:

    @property
    def first_pose(self) -> Dict[str, float]:
        return {
            'x': self.__first_pose.x,
            'y': self.__first_pose.y,
            'theta': self.__first_pose.theta,
        }

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
        self._initiated = False
        self.__first_pose = Pose()

    def get_pose(self, pose: Pose) -> None:
        self.pose_value['x'] = pose.x
        self.pose_value['y'] = pose.y
        self.pose_value['theta'] = pose.theta
        if not self._initiated:
            if pose.x != 0.0:
                self.__first_pose = pose
                self._initiated = True

    def read_pose(self) -> Dict[str, float]:
        return self.pose_value


if __name__ == "__main__":
    turtlesub = TurtleSub()
    rospy.init_node('turtle_subscriber')
    while not rospy.is_shutdown():
        turtlesub.read_pose()
