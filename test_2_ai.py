#Import the stuff needed
import pygame, sys, random
from pygame.locals import *


BLACK = 255, 255, 255

#starts pygame
pygame.init()

# the enemy ai movement timer in 1000ms
MOVE_UPPERCUT = 400
MOVE_PUNCH_LEFT = 800
MOVE_PUNCH_RIGHT = 1200
MOVE_DODGE_RIGHT = 1600
MOVE_DODGE_LEFT = 2000
MOVE_BLOCK = 2400

#figure out sprite sheet and animations and add
# AI Enemy
#ai_enemy_image = pygame.image.load("ai_spritesheet.png").convert()

#player_image = pygame.image.load("player_spritesheet.png").convert()

# Player is on sprite sheet
# each image is 82 pixels height and 40 pixels wide

# keep track of health minus for hitpoint collisions
# make the bar thingy take away for hit points
ai_health = 100
player_health = 100

# Define ai images for different moves
enemy_default  = pygame.image.load("enemy_default.png")
ai_uppercut_image = pygame.image.load("enemy_uppercut.png")
ai_l_punch_image = pygame.image.load("enemy_left.png")
ai_r_punch_image = pygame.image.load("enemy_right.png")
ai_r_dodge_image = pygame.image.load("enemy_dodge_right.png")
ai_l_dodge_image = pygame.image.load("enemy_dodge_left.png")

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

# Create a bunch of AI events 
ai_uppercut_event = pygame.USEREVENT + 1
ai_l_punch_event = pygame.USEREVENT + 2
ai_r_punch_event = pygame.USEREVENT + 3
ai_r_dodge_event = pygame.USEREVENT + 4
ai_l_dodge_event = pygame.USEREVENT + 5

enemy_x = 235
enemy_y = 145

player_x = 220
player_y = 245

movex = 10
movey = 10

aimovex = 10
aimovey = 10

activeCharacterImage = player_default
activeEnemyImage = enemy_default
 
pygame.display.set_caption("Knock'D Out!!")

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks() 

# set timer for the ai movement events
pygame.time.set_timer(ai_uppercut_event, MOVE_UPPERCUT)
pygame.time.set_timer(ai_l_punch_event, MOVE_PUNCH_LEFT)
pygame.time.set_timer(ai_r_punch_event, MOVE_PUNCH_RIGHT)
pygame.time.set_timer(ai_r_dodge_event, MOVE_DODGE_RIGHT)
pygame.time.set_timer(ai_l_dodge_event, MOVE_DODGE_LEFT)
 
# -------- Main Program Loop -----------

paused  = False
running = True

while running:
    # --- Main Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == ai_uppercut_event:
            aimovex =+ 10
            activeEnemyImage = ai_uppercut_image
            aimovex =- 10
            activeEnemyImage = enemy_default

        elif event.type == ai_l_punch_event:
            aimovey =+ 30
            aimovex =+ 10
            activeEnemyImagee = ai_l_punch_image
            aimovey =- 30
            aimovex =- 10
            activeEnemyImagee = enemy_default

        elif event.type == ai_r_punch_event:
            aimovey =- 30
            aimovex =+ 10
            activeEnemyImage = ai_r_punch_image
            aimovey =+ 30
            aimovex =- 10
            activeEnemyImage = enemy_default


        elif event.type == ai_r_dodge_event:
            aimovex =- 40
            activeEnemyImage = ai_r_dodge_image
            aimovex =+ 40
            activeEnemyImage = enemy_default

        elif event.type == ai_l_dodge_event:
            aimovey =- 10
            aimovex =- 30
            activeEnemyImage = ai_l_dodge_image
            aimovey =+ 10
            aimovex =+ 30
            activeEnemyImage = enemy_default 

        enemy_x += aimovex
        enemy_y += aimovey

        #elif event.type == reloaded_event:
            # when the reload timer runs out, reset it
            #reloaded = True
            #pygame.time.set_timer(reloaded_event, 0)

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
        screen.blit(counting_text,counting_rect)
     
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.update()
        clock.tick(25)