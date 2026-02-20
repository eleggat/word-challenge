from sys import exit
import pygame
pygame.init()


screen = pygame.display.set_mode((800, 600)) #creates the game window (width, height)
pygame.display.set_caption("Word Challenge") #sets the window title
clock = pygame.time.Clock() #creates a variable to control framerate
webkinz_font = pygame.font.Font('webkinz_book_cyrillic.otf', 32) #creates a font variable. will need to make a lot more for the board, list of words, titles, etc.

#test_surface = pygame.image.load('images/test_image.png').convert_alpha()
background = pygame.Surface((800,600))
background.fill((170, 230, 250))
#text_surface = webkinz_font.render('Hello World!', True, 'White')

clicked = False #define a global variable for use with the tiles

#tilemap = [
#    [outer1, outer2, outer3, outer4, outer5],
 #   [outer6, middle1, middle2, middle3, outer7],
  #  [outer8, middle4, centertile, middle5, outer9],
   # [outer10, middle6, middle7, middle8, outer11],
    #[outer12, outer13, outer14, outer15, outer16]
#]

#define the tile class
class Tile():

    tile_color = (205, 55, 225)
    hover_color = (245, 130, 255)
    clicked_color = (255, 230, 60)
    text_color = (0, 0, 0)
    width = height = 85

    def __init__(self, x, y, letter, score):
        self.x = x #tile x position
        self.y = y #tile y position
        self.letter = letter
        self.score = score

    def drawtile(self):

        global clicked
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

outertile1 = Tile(0+85*0, 0+85*0, "1", "0")
outertile2 = Tile(0+85*1, 0+85*0, "2", "0")
outertile3 = Tile(0+85*2, 0+85*0, "3", "0")
outertile4 = Tile(0+85*3, 0+85*0, "4", "0")
outertile5 = Tile(0+85*4, 0+85*0, "5", "0")
outertile6 = Tile(0+85*4, 0+85*1, "6", "0")
outertile7 = Tile(0+85*4, 0+85*2, "7", "0")
outertile8 = Tile(0+85*4, 0+85*3, "8", "0")
outertile9 = Tile(0+85*4, 0+85*4, "9", "0")
outertile10 = Tile(0+85*3, 0+85*4, "10", "0")
outertile11 = Tile(0+85*2, 0+85*4, "11", "0")
outertile12 = Tile(0+85*1, 0+85*4, "12", "0")
outertile13 = Tile(0+85*0, 0+85*4, "13", "0")
outertile14 = Tile(0+85*0, 0+85*3, "14", "0")
outertile15 = Tile(0+85*0, 0+85*2, "15", "0")
outertile16 = Tile(0+85*0, 0+85*1, "16", "0")
innertile1 = Tile(0+85*1, 0+85*1, "1", "0")
innertile2 = Tile(0+85*2, 0+85*1, "2", "0")
innertile3 = Tile(0+85*3, 0+85*1, "3", "0")
innertile4 = Tile(0+85*3, 0+85*2, "4", "0")
innertile5 = Tile(0+85*3, 0+85*3, "5", "0")
innertile6 = Tile(0+85*2, 0+85*3, "6", "0")
innertile7 = Tile(0+85*1, 0+85*3, "7", "0")
innertile8 = Tile(0+85*1, 0+85*2, "8", "0")
centertile = Tile(0+85*2, 0+85*2, "1", "0")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #adds the X button to the game window
            pygame.quit()
            exit()

    screen.blit(background, (0,0))
    #screen.blit(text_surface, (100,100))

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