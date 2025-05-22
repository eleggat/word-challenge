#!/usr/bin/env python

"""
Script for the word challenge game
"""

"""

- Create a list of letters with points: 16 outer, 8 middle, 1 inner
	- Probability distribution so that vowels and common consonants are more common
	- Assign all letters 3 point values (as a dictionary), one for each ring

- Assign each letter a unique position
- Select letters (by location), create string, if string matches dictionary word, then add to word lists and replace letters, else raise error
	- Should print total string after each selection
	- Needs submit button

- Shuffle function for changing order of letters within a ring

- Clear function to remove 

"""


# Imports
import csv


# Objects

#word list
with open('scrabble-words.txt', 'r') as infile:
	words_dirty = infile.read()
words = words_dirty.split("\n")[2:]

#dictionary of letters and point values {letter : [outer, middle, inner]}
with open('../word-challenge/letter-points.csv', mode='r', encoding='utf-8-sig') as infile:
	reader = csv.reader(infile)
	letters = {rows[0]:rows[1:4] for rows in reader}

for points in letters.values(): #make sure all points are integers
	for i in range(len(points)):
		points[i] = int(points[i])

#letter probabilities
inverses = {letter: 1 / points[0] for letter, points in letters.items()}
inverses_total = sum(inverses.values())
letters_probs = {letter: inv / inverses_total for letter, inv in inverses.items()}

#empty letter rings
outer = [None] * 16
middle = [None] * 8
inner = [None]


# Functions

def letter_place():
	#assign letters to positions


def word_write():
	#select letters by position and check against word list. needs printing and submitting functionality


def shuffle():
	#shuffle letters position


def clear():
	#clear current letter selection. maybe this goes inside of word writing function?




