import pygame
from json import data


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
font = pygame.font.SysFont(None, 32)
 


def texts(score):
	font=pygame.font.Font(None,30)
	scoretext=font.render("Score:"+str(score), 1,(255,255,255))
	screen.blit(scoretext, (500, 457))

#Location of number of hearts (120, 50)
def texts(hearts):
	font=pygame.font.Font(None,30)
	heartstext=font.render(str(hearts), 1,(255,255,255))
	screen.blit(heartstext, (120, 50)

#Location of number of stars (60, 50)
def texts(stars):
	font=pygame.font.Font(None,30)
	starstext=font.render(str(stars), 1,(255,255,255))
	screen.blit(starstext, (60, 50)

#Location of text for the timer (425, 35)
def texts(timer):
	font=pygame.font.Font(None,32)
	timertext=font.render(str(timer), 1,(255,255,255))
	screen.blit(timertext, (425, 35)


pygame.display.set_caption("TEST TEXT ON MATCH")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()


        screen.fill(BLACK)
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects("KNOCK'D OUT!!!", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        screen.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(60)
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
    # --- Drawing code should go here
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
    screen.blit(score, hearts, timer, stars)
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 25 frames per second
    clock.tick(60)
 
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()