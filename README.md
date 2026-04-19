- A/B test log: `projectA_moveit2/results/results.csv`## Project A — MoveIt2 Motion Planning (ROS2 Humble)
- ✅ Demo: `projectA_moveit2/assets/demo_v0_1.mp4` (click to preview)
- ✅ Details: `projectA_moveit2/README.md`
- Environment: Win11 + WSL2 Ubuntu 22.04, ROS2 Humble, RViz2 (software rendering)
# Robotics Portfolio (2026)

Hi, I'm Banana. 

## Project A — MoveIt2 Demo (ROS2 Humble)
- Demo video: `projectA_moveit2/assets/demo_v0_1.mp4`
- How to run:
```bash
source /opt/ros/humble/setup.bash
source ~/ws_moveit2/install/setup.bash
export LIBGL_ALWAYS_SOFTWARE=1
ros2 launch moveit2_tutorials demo.launch.py
# Robotics Portfolio (2026)

Hi, I'm Banana.  
### Project A — MoveIt2 Demo (ROS2 Humble)
- **What:** Motion planning in RViz2 (Plan + Execute)
- **Demo video:** `projectA_moveit2/assets/demo_v0_1.mp4`
- **How to run:**
```bash
source /opt/ros/humble/setup.bash
source ~/ws_moveit2/install/setup.bash
export LIBGL_ALWAYS_SOFTWARE=1
ros2 launch moveit2_tutorials demo.launch.py
---
## Project B — MoveIt Franka Panda Arm Motion Planning (ROS Noetic)
✅ Fully completed & verified local practice, core Hiwi skills for RWTH Aachen Robotics Lab

### Project Overview
7-DOF Franka Emika Panda robotic arm motion planning system based on ROS Noetic & MoveIt!.
Covers all daily operation skills of robotics Hiwi/research assistant in German robotics laboratories.

### Environment
- Ubuntu 20.04 LTS
- ROS Noetic Ninjemys
- MoveIt! Framework
- Franka Emika Panda manipulator model
- RViz interactive visualization

### Implemented Functions
1. Complete ROS & MoveIt environment construction, debugging and error fixing
2. Joint space free drag & motion planning
3. Cartesian linear end-effector straight path planning
4. Custom scene obstacle adding
5. Collision-aware automatic obstacle avoidance planning (robot arm automatically detours obstacles)

### Quick Start
```bash
roscore
roslaunch panda_moveit_config demo.launch
