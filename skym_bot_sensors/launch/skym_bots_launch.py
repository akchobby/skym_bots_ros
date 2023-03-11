from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    camera_parameters=[
                        {"device_id":3},
                        {"width": 640},
                        {"height":480}
                    ]

    return LaunchDescription([
        Node(
            package='image_tools',
            namespace='coral',
            executable='cam2image',
            name='camera',
            parameters=camera_parameters
        ),
        Node(
            package='bme688_driver',
            namespace='bme688',
            executable='bme688_driver.py',
            name='gas_sensor'
        )
    ])
