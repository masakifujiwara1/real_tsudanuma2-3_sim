cmake_minimum_required(VERSION 3.5)
project(real_tsudanuma2-3_sim)

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rclpy REQUIRED)
find_package(std_msgs REQUIRED)

# Add executable
# add_executable(my_node src/my_node.cpp)

# Add dependencies to executable
# ament_target_dependencies(my_node rclcpp std_msgs)

# Install executable
# install(TARGETS my_node DESTINATION lib/${PROJECT_NAME})

# Finish package
ament_package()
