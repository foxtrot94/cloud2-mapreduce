#!/bin/sh
module load hadoop
rm -rf output
hadoop jar $HADOOP_DIR/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar -input nms_airborne_radioactivity_ssn_radioactivite_dans_air.csv -output output -mapper "python3 map.py" -reducer "python3 reduce.py"

