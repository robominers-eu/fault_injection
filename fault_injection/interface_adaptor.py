from ament_index_python.packages import get_package_share_directory
import os, subprocess

interface_name_val = 'pointcloud_to_laserscan'
fi_pkg = get_package_share_directory('fault_injection')
path = os.path.join(fi_pkg, 'config', 'interfaces_definition.yaml')
template = os.path.join(fi_pkg, 'template.launch.py')

with open(template, 'r') as file:
        content = file.read()

replace = "'" + interface_name_val + "'"
substituted_content = content.replace("interface_name_val", replace)

    # Open the output file in write mode and write the substituted content
with open(template, 'w') as file:
    file.write(substituted_content)

command = "ros2 launch fault_injection template.launch.py"

# Launch the Bash command
process = subprocess.Popen(command, shell=True)