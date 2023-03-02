import os

import ament_index_python.packages
import launch
import launch_ros.actions


def generate_launch_description():
    # Get paths to packages and files
    gazebo_ros_pkg_path = ament_index_python.packages.get_package_share_directory('gazebo_ros')
    real_tsudanuma_pkg_path = ament_index_python.packages.get_package_share_directory('real_tsudanuma2-3_sim')
    turtlebot3_description_pkg_path = ament_index_python.packages.get_package_share_directory('turtlebot3_description')
    nav_cloning_pkg_path = ament_index_python.packages.get_package_share_directory('nav_cloning')
    
    # Define arguments that can be passed from command line
    script_arg = launch.substitutions.LaunchConfiguration('script', default=os.path.join(nav_cloning_pkg_path, 'scripts', 'nav_cloning_node.py'))
    mode_arg = launch.substitutions.LaunchConfiguration('mode', default='use_dl_output')
    world_name_arg = launch.substitutions.LaunchConfiguration('world_name', default=os.path.join(real_tsudanuma_pkg_path, 'world', 'willow_garage.world'))
    map_file_arg = launch.substitutions.LaunchConfiguration('map_file', default=os.path.join(real_tsudanuma_pkg_path, 'maps', 'willowgarage.yaml'))
    waypoints_file_arg = launch.substitutions.LaunchConfiguration('waypoints_file', default=os.path.join(real_tsudanuma_pkg_path, 'maps', 'willow_loop.yaml'))
    dist_err_arg = launch.substitutions.LaunchConfiguration('dist_err', default='0.8')
    initial_pose_x_arg = launch.substitutions.LaunchConfiguration('initial_pose_x', default='-10.78')
    initial_pose_y_arg = launch.substitutions.LaunchConfiguration('initial_pose_y', default='-16.78')
    initial_pose_a_arg = launch.substitutions.LaunchConfiguration('initial_pose_a', default='0.0')
    use_waypoint_nav_arg = launch.substitutions.LaunchConfiguration('use_waypoint_nav', default='false')
    use_initpose_arg = launch.substitutions.LaunchConfiguration('use_initpose', default='false')
    robot_x_arg = launch.substitutions.LaunchConfiguration('robot_x', default='0.0')
    robot_y_arg = launch.substitutions.LaunchConfiguration('robot_y', default='0.0')
    robot_Y_arg = launch.substitutions.LaunchConfiguration('robot_Y', default='0.0')

    # Set robot_description parameter
    turtlebot3_urdf_path = os.path.join(turtlebot3_description_pkg_path, 'urdf', 'turtlebot3_waffle_pi.urdf.xacro')
    turtlebot3_urdf = launch_ros.substitutions.PythonExpression(['launch.substitutions.Command(["xacro", " ', turtlebot3_urdf_path, '"])'])
    
    # Define spawn_model node
    spawn_model_node = launch_ros.actions.Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=['-entity', 'mobile_base', '-x', robot_x_arg, '-y', robot_y_arg, '-z', '0.12', '-Y', robot_Y_arg],
        parameters=[{'robot_description': turtlebot3_urdf}]
    )

    # Define initpose node
    # initpose_node = launch.actions.OpaqueFunction(function=lambda context: [
    #     launch_ros.actions.Node(
    #         package='nav_cloning',
    #         executable='initpose',
    #         name='initpose'
    #     ) if use_initpose_arg.perform(context) else None
    # ])

    # Define timed_roslaunch node
    timed_roslaunch_node = launch.actions.OpaqueFunction(function=lambda context: [
        # launch_ros.actions.Node(
        #     package='timed_roslaunch',
        #     executable='timed_roslaunch.sh',
        #     arguments=['5', 'nav_cloning', 'nav_cloning.launch', 'script:={}'.format(script_arg)],
        #     name='timed_roslaunch'
        # ),
        launch_ros.actions.Node(
            package='timed_roslaunch',
            executable='timed_roslaunch.sh',
            arguments=['8', 'real_tsudanuma2-3_sim', 'turtlebot3_navigation.launch', 'model:=waffle_pi', 'map_file:={}'.format(map_file_arg), 'waypoints_file:={}'.format(waypoints_file_arg), 'dist_err:={}'.format(dist_err_arg), 'initial_pose_x:={}'.format(initial_pose_x_arg), 'initial_pose_y:={}'.format(initial_pose_y_arg), 'initial_pose_a:={}'.format(initial_pose_a_arg), 'use_waypoint_nav:={}'.format(use_waypoint_nav_arg)],
            name='timed_roslaunch2'
        )
        # ,
        # launch_ros.actions.Node(
        #     package='timed_roslaunch',
        #     executable='timed_roslaunch.sh',
        #     arguments=['20', 'nav_cloning', 'start_wp_nav.launch'],
        #     name='timed_roslaunch3'
        # )
    ])