for i in `seq 1`
do
  roslaunch real_tsudanuma2-3_sim nav_cloning_sim_without.launch script:=nav_cloning_with_direction_node_graph.py mode:=selected_training world_name:=tsudanuma_scan.world map_file:=real_tsudanuma2-3.yaml waypoints_file:=cit3f_way_scenario.yaml dist_err:=1.0 initial_pose_x:=-5.0 initial_pose_y:=7.7 initial_pose_a:=3.14 use_waypoint_nav:=true robot_x:=-1.75 robot_y:=-3.60 robot_Y:=0.0
  sleep 10
done