#Import the stuff needed
import pygame, sys, random
from pygame.locals import *
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
# Set the height and width of the screen
size = [512, 448]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("KNOCK'D OUT!! SPLASH")

# pick background image change with enemy maybe
background1 = pygame.image.load("background_mini.png")
prematch1 = pygame.image.load("prematch_splash_mini.png")
startscr1 = pygame.image.load("startscreen_splash_mini.png")

# Define ai images for different moves
enemy_default = pygame.image.load("enemy_default.png")
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

# Star position for enemy should also be the position he defualts back too
enemy_x = 235
enemy_y = 145

# Star position for the player
player_x = 220
player_y = 245


movex = 10
movey = 10

aimovex = 10
aimovey = 10

direction = (0,0)

activeCharacterImage = player_default
activeEnemyImage = enemy_default
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks() 
 
# Starting position of the rectangle
rect_x = 50
rect_y = 50
 
# Speed and direction of rectangle
rect_change_x = 5
rect_change_y = 5
 
# This is a font we use to draw text on the screen (size 36)
font = pygame.font.Font(None, 36)
 
display_instructions = True
instruction_page = 1
 
# -------- Instruction Page Loop -----------
while not done and display_instructions:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            instruction_page += 1
            if instruction_page == 3:
                display_instructions = False
 
    # Set the screen background
    screen.fill(BLACK)
    screen.blit(startscr1,(0,0))
 
    if instruction_page == 1:
        # Draw instructions, page 1
        # This could also load an image created in another program.
        # That could be both easier and more flexible.
        text = font.render("Splash", True, WHITE)
        screen.blit(text, [10, 10])
 
        text = font.render("Page 1", True, WHITE)
        screen.blit(text, [10, 40])
 
    if instruction_page == 2:
        # Draw instructions, page 2
        screen.blit(prematch1,(0,0))
        text = font.render("Prematch Screen", True, WHITE)
        screen.blit(text, [10, 10])
 
        text = font.render("Page 2", True, WHITE)
        screen.blit(text, [10, 40])

    if instruction_page == 3:
        # Draw instructions, page 3
        text = font.render("Main Match", True, WHITE)
        screen.blit(text, [10, 10])
 
        text = font.render("Page 3", True, WHITE)
        screen.blit(text, [10, 40])

 
    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # Set the screen background
    screen.fill(BLACK)
    screen.blit(background1,(0,0))
    screen.blit(activeEnemyImage,(enemy_x,enemy_y))
    screen.blit(activeCharacterImage,(player_x,player_y))
 
    # Draw the rectangle
    pygame.draw.rect(screen, WHITE, [rect_x, rect_y, 50, 50])
 
    # Move the rectangle starting point
    rect_x += rect_change_x
    rect_y += rect_change_y
 
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
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()