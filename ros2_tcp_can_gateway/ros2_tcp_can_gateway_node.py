#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from .can2tcp.can2tcp import SocketCANGateway, TCPCanGateway


class MyTcpCanNode(Node):
    def __init__(self):
        super().__init__("tcp_can_gateway_node")
        self.declare_parameter("can_interface", "vcan0")
        self.declare_parameter("gateway_host", "192.168.1.4")
        self.declare_parameter("gateway_port", 20001)
        self.can_interface_ = self.get_parameter("can_interface").value
        self.gateway_host_ = self.get_parameter("gateway_host").value
        self.gateway_port_ = self.get_parameter("gateway_port").value
        self.get_logger().info(f"TCP/CAN gateway node has been started on interface {self.can_interface_} for host {self.gateway_host_}:{self.gateway_port_}")
        self.tcp_can_gateway_ = TCPCanGateway(self.gateway_host_, self.gateway_port_)
        self.socket_can_gateway_ = SocketCANGateway(interface=self.can_interface_, bitrate=1000000)
        self.tcp_can_gateway_.set_receive_callback(self.socket_can_gateway_.send)
        self.socket_can_gateway_.set_receive_callback(self.tcp_can_gateway_.send)


def main(args=None):
    rclpy.init(args=args)
    node = MyTcpCanNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
