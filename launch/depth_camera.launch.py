from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time')


    pcl2laser_cmd = Node(
        package='pointcloud_to_laserscan',
        executable='pointcloud_to_laserscan_node',
        name='pointcloud_to_laser',
        remappings=[('cloud_in', '/rgbd_camera/points'),
                    ('scan', '/scan')],
        parameters=[{
            'target_frame': 'd_435_camera',
            'transform_tolerance': 0.01,
            'min_height': 0.0,
            'max_height': 1.0,
            'angle_min': -1.5708,  # -M_PI/2
            'angle_max': 1.5708,  # M_PI/2
            'angle_increment': 0.0087,  # M_PI/360.0
            'scan_time': 0.3333,
            'range_min': 0.45,
            'range_max': 4.0,
            'use_inf': True,
            'inf_epsilon': 1.0
        }],
    )

    return LaunchDescription([
        DeclareLaunchArgument('use_sim_time', default_value=['True'],
                              description='use sim time from /clock'),
        pcl2laser_cmd,
   
    ])
