#!/bin/bash

# Javier E. Fajardo
# COEN498 PP: Cloud Computing
# This script is intended to be run only for debugging purposes

cat nms_airborne_radioactivity_ssn_radioactivite_dans_air.csv | ./map.py | sort | ./reduce.py 