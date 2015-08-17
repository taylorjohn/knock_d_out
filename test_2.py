#Import the stuff needed
import pygame, sys, random
from pygame.locals import *


BLACK = 255, 255, 255

#starts pygame
pygame.init()

# Define ai images for different moves
enemy_default = pygame.image.load("enemy_default.png")
enemy_left = pygame.image.load("enemy_left.png")
enemy_right = pygame.image.load("enemy_right.png")

# Define player images for different moves
player_up = pygame.image.load("player_up.png")
player_down = pygame.image.load("player_down.png")
player_default = pygame.image.load("player_default.png")
player_left = pygame.image.load("player_left.png")
player_right = pygame.image.load("player_right.png")

# pick background image change with enemy maybe
background1 = pygame.image.load("background_mini.png")
 
# Set the width and height of the screen [width, height]
size = (512, 448)
screen = pygame.display.set_mode(size)
font = pygame.font.SysFont(None, 32)

enemy_x = 235
enemy_y = 145

player_x = 220
player_y = 245

movex = 10
movey = 10

activeCharacterImage = player_default
activeEnemyImage = enemy_default
 
pygame.display.set_caption("Knock'D Out!!")

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks() 
 
# -------- Main Program Loop -----------

paused  = False
running = True

while running:
    # --- Main Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            if event.key == pygame.K_SPACE:
                paused = not paused

        # --- Event Processing ---
 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                movex =- 10
                activeCharacterImage = player_left

            elif event.key == pygame.K_RIGHT:
                movex =+ 10
                activeCharacterImage = player_right

            elif event.key == pygame.K_UP:
                movey =- 10
                activeCharacterImage = player_up

            elif event.key == pygame.K_DOWN:
                movey =+ 10
                activeCharacterImage = player_down
        else:
            activeCharacterImage = player_default
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                movex = 0
            elif event.key == pygame.K_RIGHT:
                movex = 0
            elif event.key == pygame.K_UP:
                movey = 0
            elif event.key == pygame.K_DOWN:
                movex = 0

        player_x += movex
        player_y += movey


    if not paused:
        counting_time = pygame.time.get_ticks() - start_time

        # change milliseconds into minutes, seconds, milliseconds
        counting_minutes = str(counting_time/60000) #.zfill(2)
        counting_seconds = str(((counting_time%60000)/10000)) #.zfill(2)

        counting_string = "%s:%s" % (counting_minutes, counting_seconds)

        counting_text = font.render(str(counting_string), 1, (255,255,255))
        counting_rect = (425, 35)
 
        # --- Game logic should go here
     
        # --- Drawing code should go here
     
        # First, clear the screen to black. Don't put other drawing commands
        # above this, or they will be erased with this command.
        screen.fill(BLACK)
        screen.blit(background1,(0,0))
        screen.blit(activeEnemyImage,(enemy_x,enemy_y))
        screen.blit(activeCharacterImage,(player_x,player_y))
        screen.blit(counting_text, counting_rect)
     
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.update()
        clock.tick(25)
 