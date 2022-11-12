#!/bin/bash

gnome-terminal -- bash -c "sh experiment_cit3f_without_move_base.sh ; bash"

sleep 20

gnome-terminal -- bash -c "roslaunch aisle_classification aisle_class.launch; bash"

gnome-terminal -- bash -c "roslaunch weighted_graph weighted_graph.launch; bash"