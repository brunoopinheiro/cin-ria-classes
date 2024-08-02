#! /usr/bin/python3

import rospy
from sensor_msgs.msg import LaserScan
from math import inf


class ScanSub:

    def __init__(self):
        self.sub = rospy.Subscriber(
            '/scan_raw',
            LaserScan,
            self.callback,
            queue_size=1,
        )
        self.__closest_obj = inf

    def callback(self, msg: LaserScan):
        ranges = msg.ranges[21:-21]
        min_range = inf
        for r in ranges:
            if r < min_range:
                min_range = r
        self.__closest_obj = min_range

    @property
    def closest_obj(self) -> float:
        return self.__closest_obj


if __name__ == "__main__":
    rospy.init_node('TIAGo_scan_custom_node')
    scansub = ScanSub()

    while not rospy.is_shutdown():
        print("Object at: ", scansub.closest_obj)
        if scansub.closest_obj < 0.5:
            print(f"{scansub.closest_obj}", end='\rWARNING!     ')
        else:
            print(f"{scansub.closest_obj}", end='\rSAFE DISTANCE')
