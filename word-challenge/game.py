#!/usr/bin/env python

"""
Script for the word challenge game
"""

"""
- Assign each letter a unique position
- Select letters (by location), create string, if string matches dictionary word, then add to word lists and replace letters, else raise error
	- Should print total string after each selection
	- Needs submit button

- Shuffle function for changing order of letters within a ring

- Clear function to remove 

"""


# Imports
import csv
import numpy as np


# Objects

#word list
with open('../word-challenge/scrabble-words.txt', 'r') as infile:
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

let = list(letters_probs.keys()) #only letters
let_prob = list(letters_probs.values()) #only probabilities




# Creating the Game class

class Game:
	"""
	Creating a class, which will be initiated each time the game is begun and after a word is submitted
	"""

    def __init__(self):
        self.outer = np.random.choice(let, size = 16, p = let_prob).tolist()
        self.middle = np.random.choice(let, size = 8, p = let_prob).tolist()
        self.inner = np.random.choice(let, size = 1, p = let_prob).tolist()

    def __repr__(self):
        return "Play a word game!"



def word_write():
	#select letters by position and check against word list. needs printing and submitting functionality



def shuffle():
	#shuffle letters position


def clear():
	#clear current letter selection. maybe this goes inside of word writing function?




