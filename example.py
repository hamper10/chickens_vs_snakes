import pygame
import dumbmenu as dm
pygame.init()

# Just a few static variables
red   = 255,  0,  0
green =   0,255,  0
blue  =   0,  0,255

size = width, height = 650,500	
screen = pygame.display.set_mode(size)
screen.fill(blue)
pygame.display.update()
pygame.key.set_repeat(500,30)

choose = dm.dumbmenu(screen, [
                        'Start Game',
                        'Credits',
                        'Instructions',
                        'Change Difficulty to Impossible',
                        'Quit Game'], 64,64,None,32,1.4,green,red)

if choose == 0:
    import Gamecompleteeasy as dm
elif choose == 1:
    import credits as dm
elif choose == 2:
    import instructions as dm
elif choose == 3:
    import Gamecompleteimpossible as dm
    
elif choose == 4:
    print ("You choose 'Quit Game'.")
pygame.quit()
exit()
