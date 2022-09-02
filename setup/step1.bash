#!/bin/bash -xve

dir=$(cd $(dirname $0)/..;pwd)
echo ${dir}

echo "export GAZEBO_MODEL_PATH=${dir}/models:\${GAZEBO_MODEL_PATH}" >> ~/.bashrc

echo '***INSTRUCTION*****************'
echo '* do the following command    *'
echo '* $ source ~/.bashrc          *'
echo '*******************************'