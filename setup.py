from setuptools import find_packages, setup
from glob import glob

package_name = 'ros2_tcp_can_gateway'

setup(
    name=package_name,
    version='0.0.0',
    # packages=find_packages(exclude=['test']),
    packages=["ros2_tcp_can_gateway", "ros2_tcp_can_gateway/can2tcp"],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ("share/" + package_name, glob("launch/*launch.[pxy][yma]*")),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='belovictor',
    maintainer_email='belovictor@gmail.com',
    description='A gateway node to connect local vcan interface to remote gateway over TCP',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "ros2_tcp_can_gateway_node = ros2_tcp_can_gateway.ros2_tcp_can_gateway_node:main",
        ],
    },
)
