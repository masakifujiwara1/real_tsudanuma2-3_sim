for i in `seq 1`
do
  roslaunch real_tsudanuma2-3_sim nav_cloning_sim.launch script:=nav_cloning_node_viz.py mode:=use_dl_output world_name:=tsudanuma_scan.world map_file:=real_tsudanuma2-3.yaml waypoints_file:=cit_3f_without_direction_way.yaml dist_err:=1.2 initial_pose_x:=-9.78 initial_pose_y:=29.78 initial_pose_a:=-1.57 use_waypoint_nav:=true robot_x:=-1.6 robot_y:=-3.9 robot_Y:=0.0 use_update_amcl_param:=true
  sleep 20
done