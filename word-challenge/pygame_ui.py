from sys import exit
import pygame
from game import Game, Tile
pygame.init()


screen = pygame.display.set_mode((800, 600)) #creates the game window (width, height)
pygame.display.set_caption("Word Challenge") #sets the window title
clock = pygame.time.Clock() #creates a variable to control framerate
webkinz_font = pygame.font.Font('webkinz_book_cyrillic.otf', 32) #creates a font variable. will need to make a lot more for the board, list of words, titles, etc.

#test_surface = pygame.image.load('images/test_image.png').convert_alpha()
background = pygame.Surface((800,600))
background.fill((170, 230, 250))
#text_surface = webkinz_font.render('Hello World!', True, 'White')

#tilemap = [
#    [outer1, outer2, outer3, outer4, outer5],
 #   [outer6, middle1, middle2, middle3, outer7],
  #  [outer8, middle4, centertile, middle5, outer9],
   # [outer10, middle6, middle7, middle8, outer11],
    #[outer12, outer13, outer14, outer15, outer16]
#]

############### QUESTIONS ################
#
# - Does the dictionary/points csv need to be called inside of the game run?
#
#
##########################################

# Run the game

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #adds the X button to the game window
            pygame.quit()
            exit()

    screen.blit(background, (0,0)) #establish background
    #screen.blit(text_surface, (100,100))

    # Play ten rounds
    for i in range(10):

        new_round = Game() #new round

        # assign tiles letters and points (tbd on points)
        ot1 = Tile(0+85*0, 0+85*0, f"{new_round.outer[0]}", "0")
        ot2 = Tile(0+85*1, 0+85*0, f"{new_round.outer[1]}", "0")
        ot3 = Tile(0+85*2, 0+85*0, f"{new_round.outer[2]}", "0")
        ot4 = Tile(0+85*3, 0+85*0, f"{new_round.outer[3]}", "0")
        ot5 = Tile(0+85*4, 0+85*0, f"{new_round.outer[4]}", "0")
        ot6 = Tile(0+85*4, 0+85*1, f"{new_round.outer[5]}", "0")
        ot7 = Tile(0+85*4, 0+85*2, f"{new_round.outer[6]}", "0")
        ot8 = Tile(0+85*4, 0+85*3, f"{new_round.outer[7]}", "0")
        ot9 = Tile(0+85*4, 0+85*4, f"{new_round.outer[8]}", "0")
        ot10 = Tile(0+85*3, 0+85*4, f"{new_round.outer[9]}", "0")
        ot11 = Tile(0+85*2, 0+85*4, f"{new_round.outer[10]}", "0")
        ot12 = Tile(0+85*1, 0+85*4, f"{new_round.outer[11]}", "0")
        ot13 = Tile(0+85*0, 0+85*4, f"{new_round.outer[12]}", "0")
        ot14 = Tile(0+85*0, 0+85*3, f"{new_round.outer[13]}", "0")
        ot15 = Tile(0+85*0, 0+85*2, f"{new_round.outer[14]}", "0")
        ot16 = Tile(0+85*0, 0+85*1, f"{new_round.outer[15]}", "0")
        mt1 = Tile(0+85*1, 0+85*1, f"{new_round.middle[0]}", "0")
        mt2 = Tile(0+85*2, 0+85*1, f"{new_round.middle[1]}", "0")
        mt3 = Tile(0+85*3, 0+85*1, f"{new_round.middle[2]}", "0")
        mt4 = Tile(0+85*3, 0+85*2, f"{new_round.middle[3]}", "0")
        mt5 = Tile(0+85*3, 0+85*3, f"{new_round.middle[4]}", "0")
        mt6 = Tile(0+85*2, 0+85*3, f"{new_round.middle[5]}", "0")
        mt7 = Tile(0+85*1, 0+85*3, f"{new_round.middle[6]}", "0")
        mt8 = Tile(0+85*1, 0+85*2, f"{new_round.middle[7]}", "0")
        it1 = Tile(0+85*2, 0+85*2, f"{new_round.inner[0]}", "0")


        # create lists of tile rings (lost my train of thought for why I did this)
        #outer_tiles = [ot1, ot2, ot3, ot4, ot5, ot6, ot7, ot8, ot9, ot10, ot11, ot12, ot13, ot14, ot15, ot16]
        #middle_tiles = [mt1, mt2, mt3, mt4, mt5, mt6, mt7, mt8]
        #inner_tile = [it1]

    if outertile1.drawtile():
        print("outer tile 1")
    if outertile2.drawtile():
        print("outer tile 2")
    if outertile3.drawtile():
        print("outer tile 3")
    if outertile4.drawtile():
        print("outer tile 4")
    if outertile5.drawtile():
        print("outer tile 5")
    if outertile6.drawtile():
        print("outer tile 6")
    if outertile7.drawtile():
        print("outer tile 7")
    if outertile8.drawtile():
        print("outer tile 8")
    if outertile9.drawtile():
        print("outer tile 9")
    if outertile10.drawtile():
        print("outer tile 10")
    if outertile11.drawtile():
        print("outer tile 11")
    if outertile12.drawtile():
        print("outer tile 12")
    if outertile13.drawtile():
        print("outer tile 13")
    if outertile14.drawtile():
        print("outer tile 14")
    if outertile15.drawtile():
        print("outer tile 15")
    if outertile16.drawtile():
        print("outer tile 16")
    if innertile1.drawtile():
        print("inner tile 1")
    if innertile2.drawtile():
        print("inner tile 2")
    if innertile3.drawtile():
        print("inner tile 3")
    if innertile4.drawtile():
        print("inner tile 4")
    if innertile5.drawtile():
        print("inner tile 5")
    if innertile6.drawtile():
        print("inner tile 6")
    if innertile7.drawtile():
        print("inner tile 7")
    if innertile8.drawtile():
        print("inner tile 8")
    if centertile.drawtile():
        print("center tile")



    pygame.display.update()  #updates the game window
    clock.tick(60) #sets the maximum framerate (fps)