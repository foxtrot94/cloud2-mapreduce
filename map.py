#!/usr/bin/env python3
import io
import sys
import time
import datetime

#The specific location being tracked
TRACKED_LOCATION = "Winnipeg"
#TRACKED_LOCATION = None

start = time.time()
print("{}: Started Mapping Process".format(str(datetime.datetime.now())),file=sys.stderr)

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
	
	year = column_order[2].split('-')[0]
	stat = column_order[7]
	
	print("{} {} {}".format(location, year,stat))
#end for

elapsed = time.time() - start
print("{}: Mapping Process Ended".format(str(datetime.datetime.now())),file=sys.stderr)
print("{}: Total time spent in Map {}".format(str(datetime.datetime.now()), elapsed),file=sys.stderr)
