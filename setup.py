from setuptools import find_packages, setup
from glob import glob

package_name = 'security_monitor'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),

    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),

        ('share/' + package_name, ['package.xml']),

        # IMPORTANT: install launch files
        ('share/' + package_name + '/launch', glob('launch/*.py')),
    ],

    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jetson',
    maintainer_email='jetson@todo.todo',
    description='ROS2 Security Monitoring System',
    license='MIT',

    entry_points={
        'console_scripts': [
            'camera_node = security_monitor.camera_node:main',
            'motion_detector = security_monitor.motion_detector:main',
            'alert_manager = security_monitor.alert_manager:main',
        ],
    },
)
