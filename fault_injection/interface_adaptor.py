from ament_index_python.packages import get_package_share_directory
import os, subprocess
import yaml
from yaml.loader import SafeLoader

interface_name_val = 'pointcloud_to_laserscan'
name = interface_name_val + '_node'
params_file = 'interfaces_definition.yaml'

fi_pkg = get_package_share_directory('fault_injection')
path = os.path.join(fi_pkg, 'config', 'interfaces_definition.yaml')
with open(path) as f:
    data = yaml.load(f, Loader=SafeLoader)

# print(data)
remap_list = data['pointcloud_to_laserscan_node']['ros__parameters']['remappings']
remap = " --remap " + remap_list[0] + ":=" + remap_list[1] + " --remap " + remap_list[2] + ":=" + remap_list[3]
#  launch the interface adaptor
command = "ros2 run " + interface_name_val + " " + name + " --ros-args" + remap + " --params-file " + path 
process = subprocess.Popen(command, shell=True)
