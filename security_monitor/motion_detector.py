import cv2
import numpy as np

import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image
from std_msgs.msg import String

from cv_bridge import CvBridge


class MotionDetector(Node):

    def __init__(self):

        super().__init__('motion_detector')

        self.bridge = CvBridge()

        self.previous = None

        self.subscription = self.create_subscription(
            Image,
            '/camera/image_raw',
            self.image_callback,
            10
        )

        self.alert_pub = self.create_publisher(
            String,
            '/alerts',
            10
        )

    def image_callback(self, msg):

        frame = self.bridge.imgmsg_to_cv2(
            msg,
            desired_encoding='bgr8'
        )

        gray = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2GRAY
        )

        gray = cv2.GaussianBlur(
            gray,
            (21,21),
            0
        )

        if self.previous is None:
            self.previous = gray
            return

        diff = cv2.absdiff(
            self.previous,
            gray
        )

        motion_score = np.sum(diff)

        if motion_score > 500000:

            alert = String()
            alert.data = "MOTION DETECTED"

            self.alert_pub.publish(alert)

        self.previous = gray


def main(args=None):

    rclpy.init(args=args)

    node = MotionDetector()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
