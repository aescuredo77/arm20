cmake_minimum_required(VERSION 3.0.2)
project(arm20_msg)


find_package(
  catkin REQUIRED COMPONENTS
  genmsg
  message_generation 
  std_msgs
  
)
## Generate messages in the 'msg' folder
 add_message_files(
   FILES
   jevois.msg
   xl320.msg
   cmd_robot_msg.msg
   arm_msg.msg
  )


## Generate added messages and services with any dependencies listed here
 generate_messages(
   DEPENDENCIES
   std_msgs
   xl320.msg
   jevois.msg
  )

catkin_package(
  # INCLUDE_DIRS include
  CATKIN_DEPENDS
  message_runtime 
)




