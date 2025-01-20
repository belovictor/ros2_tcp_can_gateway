import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
            'can_interface',
            default_value='vcan0',
            description='Default can interface name'
        ),
        DeclareLaunchArgument(
            'gateway_host',
            default_value='192.168.1.4',
            description='Default can gateway host'
        ),
        DeclareLaunchArgument(
            'gateway_port',
            default_value='20001',
            description='Default can gateeeway port'
        ),
        DeclareLaunchArgument(
            'node_name',
            default_value='ros2_tcp_can_gateway_node',
            description='Default node name'
        ),
        Node(
            output='screen',
            emulate_tty=True,
            package='ros2_tcp_can_gateway',
            executable='ros2_tcp_can_gateway_node',
            name=LaunchConfiguration('node_name'),
            parameters=[
                {'can_interface': LaunchConfiguration('can_interface')},
                {'gateway_host': LaunchConfiguration('gateway_host')},
                {'gateway_port': LaunchConfiguration('gateway_port')},
            ]
        ),
    ])
