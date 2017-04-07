#!/usr/bin/env python3
import io
import sys

# Data structure for holding the stats
class Stat():
	def __init__(self,):
		self.Min = 2**64
		self.Max = -self.Min
		self.Average = 0
		self.Median = 0
		self.StdDeviation = 0
		self.n = 0
		#inner vars for Standard Deviation
		self._variance = 0
		self._std_mean = 0
		self._std_n = 0
		#inner vars for Median
		
	#end init
		
	def __get_new_median(self,num):
		pass #TODO:implement
	
	def __get_new_deviation(self,num):
		"""This streaming algorithm was based on https://gist.github.com/alexalemi/2151722"""		
		self._std_n += 1
		newM = self._std_mean + (num - self._std_mean)*1./self._std_n
		newS = self._variance + (num - self._std_mean)*(num - newM)
		self._std_mean, self._variance = newM, newS
		
		if self._std_n < 2:
			return 0
		
		return (self._variance/(self._std_n-1))**(1/2)
	#end __get
	
	def update(self, num):
		self.Min = min(self.Min,num)
		self.Max = max(self.Max,num)
		
		self.Median = self.__get_new_median(num)
		self.StdDeviation = self.__get_new_deviation(num)
		self.Average = ( (self.n * self.Average) + num ) / (self.n +1)
		self.n+=1
	#end update
	
	def __str__(self):
		return "Min: {} | Max: {} | Average: {} | Median: {} | Std Dev: {}".format(self.Min,self.Max,self.Average,self.Median,self.StdDeviation)
#end class

current_location = None
current_year = None
stats = Stat()
for line in sys.stdin.buffer:
	# A bit of a hack
	clean_line = line.decode().rstrip().lstrip()
	data = clean_line.split()
	year = data[1]
	location = data[0]
	
	if current_year!=year or current_location!=location:
		if current_year is not None:
			stat_string = str(stats).replace('{','').replace('}','')
			print("{} ({})\t{}".format(current_location,current_year,stat_string))
		stats = Stat()
		current_year = year
		current_location = location
	
	# Update the current stat set
	stats.update(float(data[2]))
#end for

#Print final results
stat_string = str(stats)
print("{} ({})\t{}".format(current_location,current_year,stat_string))