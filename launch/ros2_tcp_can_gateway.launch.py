import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory



def generate_launch_description():
    return LaunchDescription([
        Node(
            output='screen',
            emulate_tty=True,
            package='ros2_tcp_can_gateway',
            executable='ros2_tcp_can_gateway_node',
            name='ros2_tcp_can_gateway_node',
            parameters=[
                {'can_interface': 'vcan0'},
                {'gateway_host': '192.168.1.4'},
                {'gateway_port': 20001},
            ]
        ),
    ])
