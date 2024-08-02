#! /usr/bin/python3

import rospy
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

rospy.init_node('move_arm')

pub = rospy.Publisher('/arm_controller/command', JointTrajectory, queue_size=1)

cmd = JointTrajectory()

cmd.joint_names.extend([
    'arm_1_joint',
    'arm_2_joint',
    'arm_3_joint',
    'arm_4_joint',
    'arm_5_joint',
    'arm_6_joint',
    'arm_7_joint',
])

point = JointTrajectoryPoint()
point.positions = [0] * 7
point.time_from_start = rospy.Duration(1)

cmd.points.append(point)

rate = rospy.Rate(1)

angle = 0.1

while not rospy.is_shutdown():

    cmd.points[0].positions[0] = angle
    cmd.points[0].time_from_start = rospy.Duration(1)

    pub.publish(cmd)
    angle += 0.1
    if angle >= 10.0:
        angle = 0.0
    rate.sleep()
