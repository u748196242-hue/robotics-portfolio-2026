# Project A — MoveIt2 Demo (ROS2 Humble)

## What
MoveIt2 demo in RViz2 (Plan + Execute). Short demo video included.

## Environment
- Windows 11 + WSL2 (Ubuntu 22.04)
- ROS2 Humble
- RViz2 software rendering: `LIBGL_ALWAYS_SOFTWARE=1`

## How to run
```bash
source /opt/ros/humble/setup.bash
source ~/ws_moveit2/install/setup.bash
export LIBGL_ALWAYS_SOFTWARE=1
ros2 launch moveit2_tutorials demo.launch.py
Demo video
assets/demo_v0_1.mp4

Experiment log (Week 1)
We recorded a simple A/B test using velocity/acceleration scaling factors.

Conditions
A: vel_scale=1.0, acc_scale=1.0

B: vel_scale=0.2, acc_scale=0.2

Metrics
plan_success (0/1)

exec_success (0/1)

planning_time_s (optional, NA if not available yet)

notes (short observation)

Data
results/results.csv

Quick takeaway (initial)
Lower scaling (0.2/0.2) looks more conservative/smoother.
Higher scaling (1.0/1.0) is faster but may appear less smooth.
