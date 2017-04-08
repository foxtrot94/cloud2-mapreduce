#!/bin/sh

# Javier E. Fajardo
# COEN498 PP: Cloud Computing
# This script is intended to be run only on the Concordia ENCS servers

rm -rf output
# NOTE: Hadoop is not enabled by default
hadoop jar $HADOOP_DIR/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar -input nms_airborne_radioactivity_ssn_radioactivite_dans_air.csv -output output -mapper "python3 map.py" -reducer "python3 reduce.py"