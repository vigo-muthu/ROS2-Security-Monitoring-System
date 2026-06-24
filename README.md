# ROS2 Security Monitoring System

A simple ROS2-based real-time security system using a camera. It captures live video, detects motion, and sends alerts using ROS2 topics.

---

# Package Structure


```text
security_monitor/
│
├── security_monitor/
│   ├── camera_node.py      # Camera stream + ROS publisher
│   ├── motion_detector.py  # Motion detection + alert publisher
│   ├── alert_manager.py    # Alert subscriber
│   └── __init__.py
│
├── launch/
│   └── security.launch.py
│
├── package.xml
└── setup.py
```

# How to Run

1. Build workspace

cd ~/ros2_ws
colcon build
source install/setup.bash

---

2. Run Camera Node

ros2 run security_monitor camera_node

---

3. Run Motion Detector

ros2 run security_monitor motion_detector

---

4. Run Alert Manager

ros2 run security_monitor alert_manager

---

# Check System

ros2 topic list

Expected output:
/camera/image_raw
/alerts
/rosout

---

Check camera stream rate:

ros2 topic hz /camera/image_raw

---

# Output

<img width="1453" height="580" alt="image" src="https://github.com/user-attachments/assets/c9c6ee50-8157-4272-86d0-66988934dc67" />


