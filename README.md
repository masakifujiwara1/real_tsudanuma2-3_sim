# real_tsudanuma2-3_sim
![Screenshot from 2024-08-31 10-29-40](https://github.com/user-attachments/assets/1869612b-af99-478d-bc15-a21c688a1e64)

## caution
world file of stable version is tsudanuma2-3_v2.3.3.world

## install
~~~
git clone -b v2.1 https://github.com/masakifujiwara1/real_tsudanuma2-3_sim.git
~~~

## setup
~~~
cd real_tsudanuma2-3_sim/setup
sh step1.bash
source ~/.bashrc
~~~

## running
~~~
cd real_tsudanuma2-3_sim/world
gazebo tsudanuma2-3_v2.3.3.world
~~~

## example of usage with ROS
https://github.com/masakifujiwara1/real_tsudanuma2-3_sim/blob/87027b53a26e68e2315eeabad6012d0c2ee0e582/launch/nav_cloning_sim.launch#L19-L28

## tested on ...
- Ubuntu 20.04 Desktop
