import yaml
from yaml.loader import SafeLoader
from launch import LaunchDescription, LaunchContext
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os
from launch.substitutions import LaunchConfiguration
import launch_ros.actions

def get_remaps(remappings_list):
    tuples_list = [tuple(item) for item in remappings_list]
    return tuples_list
    
def generate_launch_description():
    fi_pkg = get_package_share_directory('fault_injection')
    path = os.path.join(fi_pkg, 'config', 'interfaces_definition.yaml')
    with open(path, 'r') as file:
        yaml_data = yaml.load(file, Loader=SafeLoader)

    interface_adaptor = Node(
        package=yaml_data[interface_name_val]['package'],
        executable=yaml_data[interface_name_val]['executable'],
        name=yaml_data[interface_name_val]['name'],
        remappings = get_remaps((yaml_data[interface_name_val]['remappings'])),
        parameters=yaml_data[interface_name_val]['parameters']
    )

    return LaunchDescription([
        interface_adaptor,
    ])
