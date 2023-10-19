cmake_minimum_required(VERSION 3.0.2)
project(combine)

################
# Find Package #
################
  
find_package(catkin REQUIRED COMPONENTS 
  message_generation 
  std_msgs
  roscpp
  rospy
  )

#################
# Declare Files #
#################

generate_messages(
  DEPENDENCIES
  std_msgs
  )
  
catkin_package()
  
#########
# Build #
#########

include_directories(
  include
  ${catkin_INCLUDE_DIRS}
  )
  
add_executable(publisher src/publisher.cpp)
target_link_libraries(publisher ${catkin_LIBRARIES})
add_dependencies(publisher cpp_generate_messages_cpp)

