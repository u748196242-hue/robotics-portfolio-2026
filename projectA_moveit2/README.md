# Project A — MoveIt2 Demo (ROS2 Humble)

## What
MoveIt2 demo in RViz2 (Plan + Execute). Short demo video included.

## Environment
- Windows 11 + WSL2 (Ubuntu 22.04)
- ROS2 Humble
- RViz2 software rendering: LIBGL_ALWAYS_SOFTWARE=1

## How to run
```bash
source /opt/ros/humble/setup.bash
source ~/ws_moveit2/install/setup.bash
export LIBGL_ALWAYS_SOFTWARE=1
ros2 launch moveit2_tutorials demo.launch.py
