# Arm base in ROS #

This repository hosts the source code for the ROS < arm20 > package with the model of arm base in the Ergo Jr robot. With the modification that we have installed an electromagnet in the last joint to be able to manipulate small metal parts.

This is part of the practices that I am doing in the course MAstering Robot orerating System ROS in the ROBOCADEMY


## Key concepts covered ##
- The goal of this app is to practice with urdf and xacro, and implement it in gazebo to simulate.
- Create a model base in the stl.
- Create a xacro:macro


![image info](./arm20/pictures/model.png)



## Usage ## 


To use the `arm20` package clone this repository into the `src` folder of your catkin workspace.

Then build the workspace with `catkin_make`.


In arm.xacro can change the scale, the model was create in mm

roslaunch arm20 view_demo.launch --> to view the arm.urdf model in rviz only in cm
roslaunch arm20 display.launch   --> to view the arm.xacro model in rviz
roslaunch arm20 arm_control.launch --> working on it
roslaunch arm20 arm_world.launch  --> working on it 



