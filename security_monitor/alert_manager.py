import rclpy

from rclpy.node import Node
from std_msgs.msg import String


class AlertManager(Node):

    def __init__(self):

        super().__init__('alert_manager')

        self.subscription = self.create_subscription(
            String,
            '/alerts',
            self.alert_callback,
            10
        )

    def alert_callback(self, msg):

        self.get_logger().warn(
            f"{msg.data}"
        )


def main(args=None):

    rclpy.init(args=args)

    node = AlertManager()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
