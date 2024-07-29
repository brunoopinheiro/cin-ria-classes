#! /usr/bin/python3

import rospy
from turtlesubscriber import TurtleSub
from turtlepublisher import TurtlePublisher


def main():
    rospy.init_node('turtle_custom_node')
    subscriber = TurtleSub()
    publisher = TurtlePublisher()
    curr_pose = None
    initial_pose = None
    while initial_pose is None:
        if subscriber._initiated is not False:
            initial_pose = subscriber.first_pose
    target = initial_pose['x'] + 2
    print(f'Target Acquired: {target}')
    while not rospy.is_shutdown():
        curr_pose = subscriber.pose_value
        print(curr_pose)
        curr_x = curr_pose['x']
        pos_err = target - curr_x
        publisher.publish(
            x=pos_err,
            y=0.0,
            theta=0.0
        )
        publisher.rate.sleep()
        if curr_x >= target:
            print('Destination Reached')
            rospy.signal_shutdown(reason='Destination Reached')


if __name__ == '__main__':
    main()
