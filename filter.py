#!/usr/bin/python

# Your Name
# Physics 91SI Spring 2013
# Lab #4, Part 3 

# Command-line stream processing
#
# <your documentation goes here>
#

import sys

def echo(line):
	"""Stupid filter - works like echo"""
	print line

def firstword(line):
	"""Prints just the first word of each line"""
	print line.split()[0]

def main():
	# Get the first line
	line = sys.stdin.readline()

	# Change this to whatever function you want, defined above
	# You can even use a conditional based on what the first line looks like!
	filter_func = echo

	# Keep reading from stdin and filtering line by line
	while line:
		filter_func(line)
		line = sys.stdin.readline()

if __name__ == '__main__':
	main()
