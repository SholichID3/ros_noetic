cmake_minimum_required(VERSION 3.0.2)
project(cpp)

################
# Find Package #
################
  
find_package(catkin REQUIRED COMPONENTS 
  message_generation 
  rostime 
  std_msgs
  roscpp
  genmsg
  )

#################
# Declare Files #
#################

add_message_files(
  FILES
  DataType.msg
  )

add_service_files(
  FILES
  AddTwoInts.srv
  )
  
generate_messages(
  DEPENDENCIES
  std_msgs
  )
  
catkin_package(
  LIBRARIES ${PROJECT_NAME}
  CATKIN_DEPENDS 
    std_msgs 
    message_runtime
  )
  
#########
# Build #
#########

include_directories(
  include
  ${catkin_INCLUDE_DIRS}
  )
  
add_executable(publisher_str src/publisher/publisher_str.cpp)
target_link_libraries(publisher_str ${catkin_LIBRARIES})
add_dependencies(publisher_str cpp_generate_messages_cpp)

add_executable(publisher_int src/publisher/publisher_int.cpp)
target_link_libraries(publisher_int ${catkin_LIBRARIES})
add_dependencies(publisher_int cpp_generate_messages_cpp)

add_executable(publisher_msg src/publisher/publisher_msg.cpp)
target_link_libraries(publisher_msg ${catkin_LIBRARIES})
add_dependencies(publisher_msg cpp_generate_messages_cpp)

add_executable(subscriber_str src/subscriber/subscriber_str.cpp)
target_link_libraries(subscriber_str ${catkin_LIBRARIES})
add_dependencies(subscriber_str cpp_generate_messages_cpp)

add_executable(subscriber_int src/subscriber/subscriber_int.cpp)
target_link_libraries(subscriber_int ${catkin_LIBRARIES})
add_dependencies(subscriber_int cpp_generate_messages_cpp)

add_executable(subscriber_msg src/subscriber/subscriber_msg.cpp)
target_link_libraries(subscriber_msg ${catkin_LIBRARIES})
add_dependencies(subscriber_msg cpp_generate_messages_cpp)

add_executable(add_two_ints_server src/service/add_two_ints_server.cpp)
target_link_libraries(add_two_ints_server ${catkin_LIBRARIES})
add_dependencies(add_two_ints_server cpp_generate_messages_cpp)

add_executable(add_two_ints_client src/client/add_two_ints_client.cpp)
target_link_libraries(add_two_ints_client ${catkin_LIBRARIES})
add_dependencies(add_two_ints_client cpp_generate_messages_cpp)

###########
# Install #
###########

install(DIRECTORY launch/ 
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/launch
  PATTERN ".svn" EXCLUDE
  )
