import pygame
from pygame.locals import *




black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
pygame.mixer.pre_init(44100,16,2,4096)
pygame.init()


#The Ring What get put where on the Ring
width = 512
height = 448

#Back Ground Image
#  Location of background image x, y

# pick background image change with enemy maybe
background1 = pygame.image.load("background_mini.png")
# Set the width and height of the screen [width, height]
size = (512, 448)
screen = pygame.display.set_mode(size)
font = pygame.font.Font(None, 32)
pygame.display.set_caption("Timer Test")


#play background music

pygame.mixer.music.load("greatfighting.ogg")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(1)

# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
frame_count = 0
frame_rate = 60
start_time = 180
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
    # Set the screen background
    screen.fill(white)
    # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
    # --- Timer going up ---
    # Calculate total seconds
    total_seconds = frame_count // frame_rate
    # Divide by 60 to get total minutes
    minutes = total_seconds // 60
    # Use modulus (remainder) to get seconds
    seconds = total_seconds % 60
    # Use python string formatting to format in leading zeros
    output_string = "{0:02}:{1:02}".format(minutes, seconds)
    # Blit to the screen
    screen.blit(background1, [0, 0])
    text = font.render(output_string, True, white)
    screen.blit(text, [420, 38])
    # --- Timer going down ---
    # Blit to the screen
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    frame_count += 1
    # Limit to 20 frames per second
    clock.tick(frame_rate)
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
