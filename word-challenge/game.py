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
import pygame
from random import shuffle



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
		print(f"outer ring: {self.outer} \nmiddle ring: {self.middle} \ncenter: {self.inner}")
		return "Play a word game!"

	def outer_select(self, opos):
		"""
		Input index positions of letters to create a list of letters in order

		Parameters:
		pos: list of letter indices from outer ring
		"""

		#check that all indices are integers or None
		if opos is not None and type(opos) is not list:
			raise ValueError("Index numbers must be given as list")

		#check the outer ring
		print(self.outer)

		#create empty list for letters to fill
		outer_letters = []

		for i, p in enumerate(opos, 1):
			if type(p) is int:
				outer_letters.append(self.outer[p])

		return outer_letters

	def middle_select(self, mpos):
		"""
		Input index positions of letters to create a list of letters in order

		Parameters:
		pos: list of letter indices from middle ring
		"""

		#check that all indices are integers or None
		if mpos is not None and type(mpos) is not list:
			raise ValueError("Index numbers must be given as list")

		#check the middle ring
		print(self.middle)

		#create empty list for letters to fill
		middle_letters = []

		for i, p in enumerate(mpos, 1):
			if type(p) is int:
				middle_letters.append(self.middle[p])

		return middle_letters

	def shuffle(self):
		"""
		Shuffle the letters in the outer and middle rings

		Output:
		Re-ordered lists of outer and middle letters
		"""

		#shuffle letters in outer and middle rings
		shuffle(self.outer)
		shuffle(self.middle)

	def word_check(self, out = None, mid = None, inn = False):
		"""
		Concatenate selected letters into a word and check it against the dictionary

		Parameters:
		out: list of indices to pass into outer_select()
		mid: list of indices to pass into middle_select()
		inn: binary of whether to include the inner letter

		Output:
		Created word and confimation of whether it is in the dictionary
		"""

		#check all types are correct
		if type(out) is not list or type(mid) is not list:
			raise ValueError("Outer and middle letters should be lists of letter positions")

		#pass list into outer_select and calculate points
		outer_let = self.outer_select(out)

		outer_pts = []
		for let in outer_let:
			pts = letters[let][0]
			outer_pts.append(pts)
		outer_tot = sum(outer_pts)

		#pass list into inner_select and calculate points
		middle_let = self.inner_select(mid)

		middle_pts = []
		for let in middle_let:
			pts = letters[let][1]
			middle_pts.append(pts)
		middle_tot = sum(middle_pts)

		#generate center letter if true, and calculate points
		if inn is True:
			inner_let = self.inner
			inner_tot = letters[inner_let][2]
		else:
			inner_let = []
			inner_tot = 0

		#concatenate lists and create a word
		letter_list = outer_let + middle_let + inner_let
		word = "".join(letter_list)

		#check word against dictionary and ensure at least 3 letters, then calculate points
		if word in words and len(word) >= 3:
			points = outer_tot + middle_tot + inner_tot
			print(f"{word} is an accepted word worth {points} points!")
		else:
			print(f"{word} is not an accepted word.")





# Creating the tile class

class Tile():

    tile_color = (205, 55, 225)
    hover_color = (245, 130, 255)
    clicked_color = (255, 230, 60)
    text_color = (0, 0, 0)
    width = height = 85

    def __init__(self, x, y, letter, score, clicked = False):
        self.x = x #tile x position
        self.y = y #tile y position
        self.letter = letter
        self.score = score

    def drawtile(self):

        #global clicked
        #clicked = False #define a global variable for use with the tiles
        action = False

        mousepos = pygame.mouse.get_pos() #variable to store the mouse position (x, y)

        tile_rect = pygame.Rect(self.x, self.y, self.width, self.height) #pygame Rect object for the tile

        # check mouseover and clicked conditions
        if tile_rect.collidepoint(mousepos):
            if pygame.mouse.get_pressed()[0] == 1:
                clicked = True
                pygame.draw.rect(screen, self.clicked_color, tile_rect)
            elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
                clicked = False
                action = True
            else:
                pygame.draw.rect(screen, self.hover_color, tile_rect)
        else:
            pygame.draw.rect(screen, self.tile_color, tile_rect)

        # add letters and score to tile
        letterimage = webkinz_font.render(self.letter, True, self.text_color).convert_alpha()
        letterwidth = letterimage.get_width()
        letterheight = letterimage.get_height()
        screen.blit(letterimage, (self.x + (self.width / 2) - (letterwidth / 2), self.y + (self.height / 2) - (letterheight / 2)))

        return action



#def clear():
	#clear current letter selection. maybe this goes inside of word writing function?




