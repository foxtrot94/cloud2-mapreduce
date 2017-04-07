#!/bin/bash
cat nms_airborne_radioactivity_ssn_radioactivite_dans_air.csv | ./map.py | sort | ./reduce.py 