for i in `seq 1`
do
  roslaunch real_tsudanuma2-3_sim nav_cloning_sim.launch script:=nav_cloning_with_direction_node.py mode:=selected_training world_name:=Tsudanuma_2-3.world map_file:=cit_3f_map.yaml waypoints_file:=cit3f_way_scenario.yaml dist_err:=1.0 initial_pose_x:=-5.0 initial_pose_y:=7.7 initial_pose_a:=3.14 use_waypoint_nav:=true robot_x:=-5.0 robot_y:=7.7 robot_Y:=3.14
  sleep 10
done