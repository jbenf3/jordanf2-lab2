#!/usr/bin/python

# Your Name
# Physics 91SI Spring 2013
# Lab #4, Part 1

# Basic statistics functions

import sys
import os
import numpy as np
from matplotlib import pyplot as plt


def histogram(values):
	"""Displays a histogram of the values - handy if you want to see what this distribution looks like."""
	plt.ion()
	plt.figure(1)
	plt.hist(np.array(values), 50)
	plt.show()


# Bonus! Don't worry about this until you've finished everything else
def find_files(ext):
	"""Returns a list of all filenames in the current directory that end with the given extension"""
	pass # Replace this with your code


def loadcsv(filename):
	"""Loads a comma-separated-value file (.csv) and returns a list of all the numerical values, ignoring comments and any malformatted data."""
	"""Function should ignore bad data, but print all comments."""
	datafile = open(filename)

	####
	# Your code goes here
	####

	# This lets you ignore bad data
	# You'll probably want it inside your loop somewhere 
	try:
		# Do something that would fail if the entry isn't a number
	except: pass

	# Files are one of the few instances where you need
	# to manually "clean up"
	datafile.close()
	return numbers


def mean(values):
	"""Calculates the mean of a list of values"""
	pass # Replace this with your code


def stdev(values):
	"""Calculates the standard deviation of a list of values"""
	pass # Replace this with your code


def mode(values):
	"""Finds the most common value, and returns a tuple (val, n) of this value and its number of occurrences."""
	pass # Replace this with your code


def median(values):
	"""Finds the median value in a list"""
	pass # Replace this with your code


def main():
	#####
	# The starter code here will call the above functions,
	# but you're welcome to modify it
	#####
	files = [sys.argv[1]]
	
	# files = find_files('.csv')
	for fname in files:
		print "file: %s" % fname
		data = loadcsv(fname)
		print "  %d points loaded" % len(data)
		print "  mean: %f" % mean(data)
		print "  stdev: %f" % stdev(data)
		print "  median: %f" % median(data)
		print "  mode: %d (frequency: %d)" % mode(data)
		# histogram(data)
		print ""

if __name__ == '__main__':
	main()
