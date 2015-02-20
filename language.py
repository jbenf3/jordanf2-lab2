#!/usr/bin/python

# Your Name
# Physics 91SI Spring 2013
# Lab #4, Part 2 

import sys
import os

# Punctuation list
PUNCT = ",.;:\'\"?!()"

# Load a corpus and build a language model
def load_model(filename):
	"""Loads a corpus file and builds a language model consisting of word:frequency.
	Converts all words to lowercase, strips punctuation, and ignores any non-alphabetic characters."""

	# This is designed to get you started - but feel free to modify it
	dictionary = {}
	f = open(filename)
	for line in f:
		#####
		# Your code goes here
		#####

	f.close()
	return dictionary


def spellcheck(word, dictionary):
	"""Spellcheck a single word against the dictionary."""
	#####
	# Your code goes here
	#####
	pass


def find_palindromes(dictionary, n=5):
	"""Finds all palindromes in the dictionary, and prints the top n by frequency."""
	#####
	# Your code goes here
	#####
	pass


def main():
	# Do whatever you want here
	pass


if __name__ == '__main__':
	main()
