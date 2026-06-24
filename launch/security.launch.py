from launch import LaunchDescription

from launch_ros.actions import Node


def generate_launch_description():

    return LaunchDescription([

        Node(
            package='security_monitor',
            executable='camera_node',
            output='screen'
        ),

        Node(
            package='security_monitor',
            executable='motion_detector',
            output='screen'
        ),

        Node(
            package='security_monitor',
            executable='alert_manager',
            output='screen'
        ),
    ])
