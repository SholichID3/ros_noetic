cmake_minimum_required(VERSION 3.0.2)
project(python)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
)

add_message_files(
  FILES
  DataType.msg
  )
  
add_service_files(
  FILES
  AddTwoInts.srv
  )
  
catkin_package()

include_directories(
  ${catkin_INCLUDE_DIRS}
)

