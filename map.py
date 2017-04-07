#!/usr/bin/env python3
import io
import sys

#input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding='ascii')

#The specific location being tracked
#TRACKED_LOCATION = "Vancouver"
TRACKED_LOCATION = None

for line in sys.stdin.buffer:
	# A bit of a hack
	clean_line = str(line)[2:].rstrip().lstrip()
	column_order = clean_line.split(',')

	# Avoid putting in the title line
	if not column_order[3].isnumeric():
		continue

	# Column order is
	# (0) Location, Province,Date,Time,AirVolume,7BeActivity,7BeUncertainty,(7) 7BeCMD
	location = "{},{}".format(column_order[0],column_order[1])
	if TRACKED_LOCATION is not None and not TRACKED_LOCATION in location:
		# skip this and keep going
		continue
	#end if
	
	year = column_order[2]
	stat = column_order[7]
	
	print("{} {} {}".format(location, year,stat))
#end for