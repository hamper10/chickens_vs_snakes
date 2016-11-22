"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
screen_width = 650
screen_height = 500
screen = pygame.display.set_mode([screen_width,screen_height])
 
pygame.display.set_caption("Instructions")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
font = pygame.font.SysFont('Calibri', 25, True, False) 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            import example as dm
            
 
    # --- Game logic should go here
 
    # --- Drawing code should go here
 
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(BLUE)

    text = font.render("""Welcome to my Game""" ,True,RED)
    screen.blit(text, [100, 10])
    text = font.render("""Control the chicken with the mouse""" ,True,RED)
    screen.blit(text, [100, 40])
    text = font.render("""Shoot with left mouse click""" ,True,RED)
    screen.blit(text, [100, 70])
    text = font.render("""Kill the hungry snakes before time runs out""" ,True,RED)
    screen.blit(text, [100, 100])
    text = font.render("""Click left mouse button to return to menu""" ,True,RED)
    screen.blit(text, [100, 130])
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
