import cv2

import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image
from cv_bridge import CvBridge


class CameraNode(Node):

    def __init__(self):
        super().__init__('camera_node')

        # ROS publisher
        self.publisher = self.create_publisher(
            Image,
            '/camera/image_raw',
            10
        )

        self.bridge = CvBridge()

        # ==================================
        # ✅ Stable Jetson Camera (V4L2)
        # ==================================
        self.cap = cv2.VideoCapture(0, cv2.CAP_V4L2)

        if not self.cap.isOpened():
            self.get_logger().error("❌ Camera failed to open")
        else:
            self.get_logger().info("✅ Camera opened successfully")

        # Timer (30 FPS)
        self.timer = self.create_timer(0.03, self.publish_frame)

    def publish_frame(self):

        ret, frame = self.cap.read()

        if not ret:
            self.get_logger().warning("⚠ No frame received from camera")
            return

        # ============================
        # ROS Publish
        # ============================
        msg = self.bridge.cv2_to_imgmsg(frame, encoding='bgr8')
        self.publisher.publish(msg)

        # ============================
        # LIVE CAMERA WINDOW (NEW)
        # ============================
        cv2.imshow("Live Camera - ROS2 Security System", frame)

        # IMPORTANT: keeps window responsive
        if cv2.waitKey(1) & 0xFF == ord('q'):
            self.get_logger().info("Shutting down camera node...")
            rclpy.shutdown()


def main(args=None):

    rclpy.init(args=args)

    node = CameraNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    # cleanup
    node.cap.release()
    cv2.destroyAllWindows()
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
