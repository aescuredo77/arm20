cmake_minimum_required(VERSION 3.0.2)
project(arm20_srv)

## Compile as C++11, supported in ROS Kinetic and newer
 add_compile_options(-std=c++11)


find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  sensor_msgs
  std_msgs
  geometry_msgs
  message_generation
)

## Generate services in the 'srv' folder
 add_service_files(
   FILES
   arm_seq_send.srv
 )


## Generate added messages and services with any dependencies listed here
generate_messages(
   DEPENDENCIES
   sensor_msgs
   std_msgs
   geometry_msgs
   arm20_msg
)

catkin_package(
  CATKIN_DEPENDS 
  roscpp 
  rospy 
  message_runtime
)

include_directories(
 include
  ${catkin_INCLUDE_DIRS}
)

catkin_install_python(
	PROGRAMS 
  scripts/send_arm_server.py
  
	DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
