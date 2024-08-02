#! /usr/bin/python3

import rospy
from sensor_msgs.msg import LaserScan
from visualization_msgs.msg import Marker
from math import inf, cos, sin


class ScanSub:

    def __init__(self):
        self.sub = rospy.Subscriber(
            '/scan_raw',
            LaserScan,
            self.callback,
            queue_size=1,
        )
        self.__closest_obj = inf
        self.pub = rospy.Publisher(
            '/marker_laser',
            Marker,
            queue_size=1,
        )

    def callback(self, msg: LaserScan):
        min_range = inf
        idx = 0
        idx_min = 0
        for r in msg.ranges:
            if r < min_range and r < 0.8:
                min_range = r
                idx_min = idx
            idx += 1

        angle = msg.angle_min + idx_min * msg.angle_increment
        x_box = min_range * cos(angle)
        y_box = min_range * sin(angle)
        mkr = Marker()
        mkr.header.frame_id = 'base_laser_link'
        mkr.type = mkr.SPHERE
        mkr.action = mkr.ADD
        # mkr.scale.x = 0.05
        # mkr.scale.y = 0.05
        # mkr.scale.z = 0.05
        mkr.scale.x = 0.05
        mkr.scale.y = 0.05
        mkr.scale.z = 0.05
        mkr.color.a = 1.0
        mkr.color.r = 1.0
        mkr.color.g = 0.0
        mkr.color.b = 1.0
        mkr.pose.position.x = x_box
        mkr.pose.position.y = y_box
        mkr.pose.position.z = 0.0
        self.pub.publish(mkr)

    @property
    def closest_obj(self):
        return self.__closest_obj

    def make_marker(self, pose) -> Marker:
        mkr = Marker()
        mkr.header.frame_id = 'base_laser_link'
        mkr.type = mkr.SPHERE
        mkr.action = mkr.ADD
        # mkr.scale.x = 0.05
        # mkr.scale.y = 0.05
        # mkr.scale.z = 0.05
        mkr.scale.x = 1.5
        mkr.scale.y = 1.5
        mkr.scale.z = 1.5
        mkr.color.a = 1.0
        mkr.color.r = 1.0
        mkr.color.g = 0.0
        mkr.color.b = 1.0
        mkr.pose.position.x = pose[0]
        mkr.pose.position.y = pose[1]
        mkr.pose.position.z = 1.0


if __name__ == "__main__":
    rospy.init_node('TIAGo_scan_closest_obj')
    scansub = ScanSub()

    while not rospy.is_shutdown():
        print("Object at: ", scansub.closest_obj)
