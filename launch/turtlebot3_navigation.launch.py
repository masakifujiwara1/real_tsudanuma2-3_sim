import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, EnvironmentVariable
from launch_ros.actions import Node

def generate_launch_description():
    # Arguments
    model = LaunchConfiguration('model', default=EnvironmentVariable('TURTLEBOT3_MODEL'))
    map_file = LaunchConfiguration('map_file', default=os.path.join(get_package_share_directory('turtlebot3_navigation'), 'maps', 'map.yaml'))
    open_rviz = LaunchConfiguration('open_rviz', default='true')
    move_forward_only = LaunchConfiguration('move_forward_only', default='false')
    waypoints_file = LaunchConfiguration('waypoints_file', default='/home/masaya/maps/waypoints_willow.yaml')
    dist_err = LaunchConfiguration('dist_err', default='0.8')
    initial_pose_x = LaunchConfiguration('initial_pose_x', default='-10.78')
    initial_pose_y = LaunchConfiguration('initial_pose_y', default='-16.78')
    initial_pose_a = LaunchConfiguration('initial_pose_a', default='0.0')
    use_waypoint_nav = LaunchConfiguration('use_waypoint_nav', default='false')
    rate = LaunchConfiguration('rate', default='3.0')
    loop = LaunchConfiguration('loop', default='true')

    # Turtlebot3
    turtlebot3_remote_launch_file_dir = os.path.join(get_package_share_directory('turtlebot3_bringup'), 'launch')
    
    # Map server
    map_server_node = Node(
        package='nav2_map_server',
        executable='map_server',
        name='map_server',
        output='screen',
        parameters=[{'yaml_filename': map_file}]
        )

    # AMCL
    amcl_node = Node(
       package='nav2_amcl',
       executable='amcl',
       name='amcl',
       output='screen',
       parameters=[{'use_sim_time': False},
                   {'initial_pose.x': initial_pose_x},
                   {'initial_pose.y': initial_pose_y},
                   {'initial_pose.a': initial_pose_a}]
       )

    # move_base
    move_base_node = Node(
       package='nav2_controller',
       executable='controller_server',
       name='controller_server',
       output='screen',
       parameters=[{'use_sim_time': False},
                   {'robot_base_frame': model},
                   {'move_forward_only': move_forward_only},
                   {'cmd_vel_topic': '/nav_vel'}]
      )

    # waypoints_nav or waypoint_nav node (depending on use_waypoint_nav argument)
    # if use_waypoint_nav == 'false':
    #   waypoints_node = Node(
    #       package='fulanghua_waypoints_nav',
    #       executable='waypoints_nav',
    #       name='waypoints_nav',
    #       output='screen',
    #       parameters=[{'filename': waypoints_file},
    #                   {'dist_err': dist_err}]
    #       )
    # else:
    #   waypoints_node = Node(
    #       package='waypoint_nav',
    #       executable='waypoint_navigator_with_direction',
    #       name='waypoint_nav',
    #       output='screen'
    #       )

    # Launch description
    ld = LaunchDescription()

    # Declare the launch options
    ld.add_action(DeclareLaunchArgument('model', default_value=model, description='model type [burger, waffle, waffle_pi]'))
    ld.add_action(DeclareLaunchArgument('map_file', default_value=map_file))
    ld.add_action(DeclareLaunchArgument('open_rviz', default_value=open_rviz))
    ld.add_action(DeclareLaunchArgument('move_forward_only', default_value=move_forward_only))
    ld.add_action(DeclareLaunchArgument('waypoints_file', default_value=waypoints_file))
    ld.add_action(DeclareLaunchArgument('dist_err', default_value=dist_err))
    ld.add_action(DeclareLaunchArgument('initial_pose_x', default_value=initial_pose_x))
    ld.add_action(DeclareLaunchArgument('initial_pose_y', default_value=initial_pose_y))
    ld.add_action(DeclareLaunchArgument('initial_pose_a', default_value=initial_pose_a))
    ld.add_action(DeclareLaunchArgument('use_waypoint_nav', default_value=use_waypoint_nav))
    ld.add_action(DeclareLaunchArgument('rate', default_value=rate))
    ld.add_action(DeclareLaunchArgument('loop', default_value=loop))

  
    # Add the actions to launch all of the navigation nodes
    ld.add_action(map_server_node)
    ld.add_action(amcl_node)
    ld.add_action(move_base_node)
    if use_waypoint_nav == 'false':
        ld.add_action(waypoints_node)
    else:
        ld.add_action(include_launch_description(LaunchDescriptionSource(turtlebot3_remote_launch_file_dir)))
        if open_rviz == 'true':
            rviz_config_dir = os.path.join(get_package_share_directory('turtlebot3_navigation2'), 'rviz')
            rviz_config = os.path.join(rviz_config_dir, 'nav2_default_view.rviz')
            rviz_node = Node(
                package='rviz2',
                executable='rviz2',
                name='rviz2',
                output='log',
                arguments=['-d', rviz_config],
                parameters=[{'use_sim_time': False}]
                )
            launch_actions.append(rviz_node)

    return launch_description