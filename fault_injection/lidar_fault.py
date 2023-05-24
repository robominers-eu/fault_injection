import rclpy 
from rclpy.node import Node 
from sensor_msgs.msg import LaserScan 
import subprocess, os, signal, sys


class LaserScanModifierNode(Node): 
    def __init__(self): 
        super().__init__('laser_scan_modifier')  

        # Create a publisher for the modified scan topic 
        self.publisher_ = self.create_publisher(LaserScan, 'scan', 30) 

        # Create a subscriber for the original scan topic 
        self.subscription_ = self.create_subscription( 
            LaserScan, 
            'scan', 
            self.scan_callback, 
            30
        ) 
        self.get_logger().info("Injecting fault: zero laser error")

        self.subscription_  # prevent unused variable warning

    def kill_ros2_node(self, process_name):
        cmd = f"pgrep -f {process_name}"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            pids = result.stdout.strip().split('\n')

        for value in pids:
                cmd = f"kill -9 {str(value)}"
                subprocess.run(cmd, shell=True, text=True)
                break
        os.kill(os.getpid(), signal.SIGINT) # kill alsocurrent node

    def scan_callback(self, msg):
        # Modify the received scan message and add the constant value
        try:
            if msg.header.frame_id == 'rm2_sim/base_link/front_lidar':
                modified_scan = msg
                # Add your constant value to the scan data
                modified_scan.ranges = [0.0] * len(msg.ranges)
                # Publish the modified scan message
                self.publisher_.publish(modified_scan)
                self.kill_ros2_node('lidar_bridge') # kill laser bridge

        except KeyboardInterrupt:
            self.get_logger().info('Shutting down lidar...')
            sys.exit()


def main(args=None): 
    rclpy.init(args=args) 
    node = LaserScanModifierNode() 
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__': 
    main() 

 