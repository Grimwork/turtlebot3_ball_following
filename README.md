# TurtleBot3 Pick yellow ball (version 0)

## Plugins

[Link attacher](https://github.com/pal-robotics/gazebo_ros_link_attacher)

## Requirement 
- [TurtleBot 3 Manipulation](https://github.com/ROBOTIS-GIT/turtlebot3_manipulation)
- [TurtleBot 3 Manipulation simulations](https://github.com/ROBOTIS-GIT/turtlebot3_manipulation_simulations)
- [Open Manipulator dependencies](https://github.com/ROBOTIS-GIT/open_manipulator_dependencies)

```bash
sudo apt install ros-noetic-ros-control* ros-noetic-control* ros-noetic-moveit*
```
## Quick Start

```bash
roslaunch turtlebot3_ball_following simulator_with_arm.launch
roslaunch turtlebot3_ball_following robot_controler.launch
```

Tracking command
```bash
rosrun turtlebot3_ball_following tracking_command.py run
rosrun turtlebot3_ball_following tracking_command.py stop
```

Manipulation command 
```bash
rosrun turtlebot3_ball_following manipulation_command.py init
rosrun turtlebot3_ball_following manipulation_command.py pick
rosrun turtlebot3_ball_following manipulation_command.py detach
rosrun turtlebot3_ball_following manipulation_command.py podium
```