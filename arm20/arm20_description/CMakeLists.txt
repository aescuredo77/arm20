cmake_minimum_required(VERSION 3.0.2)
project(arm20_description)

find_package(catkin REQUIRED COMPONENTS
  joint_state_publisher
  robot_state_publisher
  rviz
)

catkin_package()

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)
