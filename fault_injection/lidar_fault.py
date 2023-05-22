import rclpy 
from rclpy.node import Node 
from sensor_msgs.msg import LaserScan 


class LaserScanModifierNode(Node): 
    def __init__(self): 
        super().__init__('laser_scan_modifier')  

        # Create a publisher for the modified scan topic 
        self.publisher_ = self.create_publisher(LaserScan, 'scan', 10) 

        # Create a subscriber for the original scan topic 
        self.subscription_ = self.create_subscription( 
            LaserScan, 
            'scan', 
            self.scan_callback, 
            10
        ) 
        self.get_logger().info("Injecting fault: zero laser error")
        # self.subscription_.assert_liveliness() 
        # # Constant value to be added to the scan data 
        # self.constant_value_ = 0.0 

  

    def scan_callback(self, msg):
        # Modify the received scan message and add the constant value
        modified_scan = msg
        # Add your constant value to the scan data
        modified_scan.ranges = [0.0] * len(msg.ranges)

        # Publish the modified scan message
        self.publisher_.publish(modified_scan)

        # Publish the modified scan data on the new topic 
        self.publisher_.publish(modified_scan) 


def main(args=None): 
    rclpy.init(args=args) 
    node = LaserScanModifierNode() 
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__': 

    main() 

 