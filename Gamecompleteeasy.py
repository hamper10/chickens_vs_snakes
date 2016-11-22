"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
import random
import time

health=200
enemytimer=200
enemytimer1=0
time=600
arrows=[]
score = 0
highscore=[]

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

 


player_image = pygame.image.load("image/images/hunter.png")
fort = pygame.image.load("image/images/fort.png")
bullet = pygame.image.load("image/images/bullet.png")
enemy = pygame.image.load("image/images/enemy.png")
gameover = pygame.image.load("image/images/gameover.png")
grass = pygame.image.load("image/images/Grass.png")
gameover = pygame.image.load("image/images/gameover.png")
youwin = pygame.image.load("image/images/youwin.png")

#Classes
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        my_image=pygame.image.load("image/images/enemy.png")
        self.image = my_image
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x -= 3
        if self.rect.x < 100:
            self.rect.x = 670
            
        if score >= 20 and time >= 0:
            self.rect.x = 0
        if time <= 0:
            self.rect.x = 0
        
            
            
         

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        my_image=pygame.image.load("image/images/hunter.png")
        self.image = my_image
        self.rect = self.image.get_rect()

        

class Nest(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        my_image=pygame.image.load("image/images/fort.png")
        self.image = my_image
        self.rect = self.image.get_rect()



class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        my_image=pygame.image.load("image/images/bullet.png")
        self.image = my_image
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.x += 5
             
    
        
    
#Functions
def draw_bullet(screen, x, y):
    screen.blit(bullet,(x,y))

def draw_hero(screen, x, y):
    screen.blit(player_image,(x,y))

def draw_nests(screen, x, y):
    screen.blit(fort,(0,140))
    screen.blit(fort,(0,235))
    screen.blit(fort,(0,350))

def draw_enemies(screen, x, y):
    screen.blit(enemy,(640,random.randint(50,430)))

# initialize pygame
pygame.init()
 
# Set the width and height of the screen [width, height]
screen_width = 650
screen_height = 500
screen = pygame.display.set_mode([screen_width,screen_height])
pygame.display.set_caption("My Game")

# Spitie lists
enemy_list = pygame.sprite.Group()

# All Sprite List
all_sprites_list = pygame.sprite.Group()


# Bullet List
bullet_list = pygame.sprite.Group()

# Loop to make the Spirites
for i in range(20):
    # This represents a block
    enemy = Enemy()
 
    # Set a random location for the block
    enemy.rect.x = random.randrange(625,650)
    enemy.rect.y = random.randrange(screen_height-20)
 
    # Add the block to the list of objects
    enemy_list.add(enemy)
    all_sprites_list.add(enemy)
    

  

#Creating the player
player = Player()
nest = Nest()
bullet = Bullet()
all_sprites_list.add(player,nest,bullet)
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

pygame.mouse.set_visible(False)

#Create enemy and put them in list

#Add player to List

#all_sprites_list.add(player)

#create List for Bullets

#score thing
font = pygame.font.SysFont('Calibri', 25, True, False)

# -------- Main Program Loop -----------
while not done:
    time -= 1
    if time <= 0:
        time = 0
    if score >= 20:
        time += 1
        
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Fire a bullet if the user clicks the mouse button
            bullet = Bullet()
            # Set the bullet so it is where the player is
            bullet.rect.x = player.rect.x
            bullet.rect.y = player.rect.y
            # Add the bullet to the lists
            all_sprites_list.add(bullet)
            bullet_list.add(bullet)
 
    # --- Game logic should go here
    
    # --- Drawing code should go here
 
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
    screen.blit(grass, [0, 0])

    #Get dat mouse
    pos = pygame.mouse.get_pos()
    
    #Got dat mouse
    player.rect.x = pos[0]
    player.rect.y = pos[1]

    #moving the enemies + bullets
    enemy_list.update()
    bullet_list.update()
    # sprite Collide Function
    enemy_hit_list = pygame.sprite.spritecollide(bullet, enemy_list, True)

    #Check For Collisions
    for enemy in enemy_hit_list:
        score += 1
        time += 10

    #Score thing
    text = font.render("Score: " + str(score),True,BLACK)
    screen.blit(text, [300, 10])

    #time thing
    text = font.render("Time Left: " + str(time),True,WHITE)
    screen.blit(text, [100, 10])

    # Draw all the spites
    all_sprites_list.draw(screen)

    
    #Checks for winner and loser
    if score >= 20 and time >= 0:
        screen.blit(youwin, (0,0))

        
        
        
    if time <= 0:
        screen.blit(gameover, (0,0))
        
        
        
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
    
highscore.append(score)
print (highscore)
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
