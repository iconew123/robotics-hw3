cmake_minimum_required(VERSION 3.0.2)
project(algorithm)

find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  message_generation
  rospy
  Vector3_msg
)

# Generate messages in the 'msg' folder
add_message_files(
 FILES
 Vector3.msg
)


# Generate added messages and services with any dependencies listed here
generate_messages(
 DEPENDENCIES
 geometry_msgs
 Vector3_msgs
)

catkin_package(
 CATKIN_DEPENDS geometry_msgs rospy Vector3_msgs
)
