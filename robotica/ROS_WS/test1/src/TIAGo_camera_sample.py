#! /usr/bin/python3

import rospy
import cv2
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image


class TIAGoCamSubscriber:

    def __init__(self) -> None:
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber(
            '/xtion/rgb/image_color',
            Image,
            self.image_cb,
        )
        self.im_shape = [None, None]

    def image_cb(self, msg: Image):
        try:
            self.cv_image = self.bridge.imgmsg_to_cv2(
                msg,
                'bgr8',
            )

        except CvBridgeError as e:
            print(e)

        width = int(msg.width/2)
        height = int(msg.height/2)
        self.cv_image = cv2.resize(self.cv_image, (width, height))

        red_treshold = 50
        for h in range(height-1):
            for w in range(width-1):
                if self.cv_image[h, w, 2] < red_treshold:
                    self.cv_image[h, w, 0] = 203
                    self.cv_image[h, w, 1] = 192
                    self.cv_image[h, w, 2] = 255

        print(self.cv_image[0][0])

        cv2.imshow('raw', self.cv_image)
        cv2.waitKey(2)


if __name__ == "__main__":
    rospy.init_node('custom_camera')
    cam = TIAGoCamSubscriber()

    rospy.spin()
