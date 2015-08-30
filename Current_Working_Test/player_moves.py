""" player_moves.py 
    illustrates a multi-frame animation
    Responding to input and adding state and sound
"""
import pygame

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
yellow = (255, 255, 0)
red = (255, 0, 0)

pygame.mixer.pre_init(44100, 16, 2, 4096)
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

def health_bars(player_health, opponent_health):

    if player_health > 75:
        player_health_color = green
    elif player_health > 50:
        player_health_color = yellow
    else:
        player_health_color = red

    if opponent_health > 75:
        opponent_health_color = green
    elif opponent_health > 50:
        opponent_health_color = yellow
    else:
        opponent_health_color = red

    pygame.draw.rect(screen, player_health_color, (175, 33, player_health, 12))
    pygame.draw.rect(screen, opponent_health_color, (290, 33, opponent_health, 12))

class Playerone(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.STANDING = 0
        self.UPPERCUT = 1
        self.LEFTDODGE = 3
        self.RIGHTDODGE = 4
        self.LEFTBODYBLOW = 5
        self.RIGHTBODYBLOW = 6
        self.LEFTFACEPUNCH = 7
        self.RIGHTFACEPUNCH = 8
        self.DOWNDODGE = 9
        self.DOWNDUCK = 10

        self.loadImages()
        self.image = self.imageStand
        self.rect = self.image.get_rect()
        self.rect.center = (256, 348)
        self.frame = 0
        self.delay = 3
        self.pause = 0
        self.state = self.STANDING
        pygame.mixer.init()
        self.punch = pygame.mixer.Sound("jab.wav")
        self.dodge = pygame.mixer.Sound("whoosh.wav")

    def update(self):
        if self.state == self.STANDING:
            self.image = self.imageStand

        elif self.state == self.UPPERCUT:
            self.pause += 1
            if self.pause > self.delay:
                #reset pause and advance animation
                self.pause = 0
                self.frame += 1
                if self.frame >= len(self.uppercutImages):
                    self.frame = 0
                    self.state = self.STANDING
                    self.image = self.imageStand
                else:
                    self.image = self.uppercutImages[self.frame]
        elif self.state == self.LEFTDODGE:
            self.pause += 1
            if self.pause > self.delay:
                #reset pause and advance animation
                self.pause = 0
                self.frame += 1
                if self.frame >= len(self.leftdodgeImages):
                    self.frame = 0
                    self.state = self.STANDING
                    self.image = self.imageStand
                else:
                    self.image = self.leftdodgeImages[self.frame]

        elif self.state == self.RIGHTDODGE:
            self.pause += 1
            if self.pause > self.delay:
                #reset pause and advance animation
                self.pause = 0
                self.frame += 1
                if self.frame >= len(self.rightdodgeImages):
                    self.frame = 0
                    self.state = self.STANDING
                    self.image = self.imageStand
                else:
                    self.image = self.rightdodgeImages[self.frame]

        elif self.state == self.LEFTBODYBLOW:
            self.pause += 1
            if self.pause > self.delay:
                #reset pause and advance animation
                self.pause = 0
                self.frame += 1
                if self.frame >= len(self.leftbodyblowImages):
                    self.frame = 0
                    self.state = self.STANDING
                    self.image = self.imageStand
                else:
                    self.image = self.leftbodyblowImages[self.frame]

        elif self.state == self.RIGHTBODYBLOW:
            self.pause += 1
            if self.pause > self.delay:
                #reset pause and advance animation
                self.pause = 0
                self.frame += 1
                if self.frame >= len(self.rightbodyblowImages):
                    self.frame = 0
                    self.state = self.STANDING
                    self.image = self.imageStand
                else:
                    self.image = self.rightbodyblowImages[self.frame]

        elif self.state == self.LEFTFACEPUNCH:
            self.pause += 1
            if self.pause > self.delay:
                #reset pause and advance animation
                self.pause = 0
                self.frame += 1
                if self.frame >= len(self.leftfacepunchImages):
                    self.frame = 0
                    self.state = self.STANDING
                    self.image = self.imageStand
                else:
                    self.image = self.leftfacepunchImages[self.frame]

        elif self.state == self.RIGHTFACEPUNCH:
            self.pause += 1
            if self.pause > self.delay:
                #reset pause and advance animation
                self.pause = 0
                self.frame += 1
                if self.frame >= len(self.rightfacepunchImages):
                    self.frame = 0
                    self.state = self.STANDING
                    self.image = self.imageStand
                else:
                    self.image = self.rightfacepunchImages[self.frame]

        elif self.state == self.DOWNDODGE:
            self.pause += 1
            if self.pause > self.delay:
                #reset pause and advance animation
                self.pause = 0
                self.frame += 1
                if self.frame >= len(self.downdodgeImages):
                    self.frame = 0
                    self.state = self.STANDING
                    self.image = self.imageStand
                else:
                    self.image = self.downdodgeImages[self.frame]

        elif self.state == self.DOWNDUCK:
            self.pause += 1
            if self.pause > self.delay:
                #reset pause and advance animation
                self.pause = 0
                self.frame += 1
                if self.frame >= len(self.downduckImages):
                    self.frame = 0
                    self.state = self.STANDING
                    self.image = self.imageStand
                else:
                    self.image = self.downduckImages[self.frame]

    def loadImages(self):
        self.imageStand = pygame.image.load("playeroneImages/idle-e0001.png")
        self.imageStand = self.imageStand.convert()
        transColor = self.imageStand.get_at((1, 1))
        self.imageStand.set_colorkey(transColor)

        self.uppercutImages = []
        for i in range(7):
            imgName = "playeroneImages/uppercut-e000%d.png" % i
            tmpImage = pygame.image.load(imgName)
            tmpImage = tmpImage.convert()
            transColor = tmpImage.get_at((1, 1))
            tmpImage.set_colorkey(transColor)
            self.uppercutImages.append(tmpImage)

        self.leftdodgeImages = []
        for i in range(2):
            imgName = "playeroneImages/leftdodge-e000%d.png" % i
            tmpImage = pygame.image.load(imgName)
            tmpImage = tmpImage.convert()
            transColor = tmpImage.get_at((1, 1))
            tmpImage.set_colorkey(transColor)
            self.leftdodgeImages.append(tmpImage)

        self.rightdodgeImages = []
        for i in range(2):
            imgName = "playeroneImages/rightdodge-e000%d.png" % i
            tmpImage = pygame.image.load(imgName)
            tmpImage = tmpImage.convert()
            transColor = tmpImage.get_at((1, 1))
            tmpImage.set_colorkey(transColor)
            self.rightdodgeImages.append(tmpImage)

        self.leftbodyblowImages = []
        for i in range(4):
            imgName = "playeroneImages/leftbodyblow-e000%d.png" % i
            tmpImage = pygame.image.load(imgName)
            tmpImage = tmpImage.convert()
            transColor = tmpImage.get_at((1, 1))
            tmpImage.set_colorkey(transColor)
            self.leftbodyblowImages.append(tmpImage)

        self.rightbodyblowImages = []
        for i in range(4):
            imgName = "playeroneImages/rightbodyblow-e000%d.png" % i
            tmpImage = pygame.image.load(imgName)
            tmpImage = tmpImage.convert()
            transColor = tmpImage.get_at((1, 1))
            tmpImage.set_colorkey(transColor)
            self.rightbodyblowImages.append(tmpImage)

        self.leftfacepunchImages = []
        for i in range(4):
            imgName = "playeroneImages/leftfacepunch-e000%d.png" % i
            tmpImage = pygame.image.load(imgName)
            tmpImage = tmpImage.convert()
            transColor = tmpImage.get_at((1, 1))
            tmpImage.set_colorkey(transColor)
            self.leftfacepunchImages.append(tmpImage)

        self.rightfacepunchImages = []
        for i in range(4):
            imgName = "playeroneImages/rightfacepunch-e000%d.png" % i
            tmpImage = pygame.image.load(imgName)
            tmpImage = tmpImage.convert()
            transColor = tmpImage.get_at((1, 1))
            tmpImage.set_colorkey(transColor)
            self.rightfacepunchImages.append(tmpImage)

        self.downdodgeImages = []
        for i in range(2):
            imgName = "playeroneImages/downdodge-e000%d.png" % i
            tmpImage = pygame.image.load(imgName)
            tmpImage = tmpImage.convert()
            transColor = tmpImage.get_at((1, 1))
            tmpImage.set_colorkey(transColor)
            self.downdodgeImages.append(tmpImage)

        self.downduckImages = []
        for i in range(3):
            imgName = "playeroneImages/downduck-e000%d.png" % i
            tmpImage = pygame.image.load(imgName)
            tmpImage = tmpImage.convert()
            transColor = tmpImage.get_at((1, 1))
            tmpImage.set_colorkey(transColor)
            self.downduckImages.append(tmpImage)

pygame.display.set_caption("Testing Player Moves")

background = pygame.Surface(screen.get_size())
background.fill((0, 0x99, 0))
screen.blit(background, (0, 0))

playerone = Playerone()
allSprites = pygame.sprite.Group(playerone)

clock = pygame.time.Clock()
# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
frame_count = 0
frame_rate = 60
start_time = 180

#in game loop
player_health = 100
opponent_health = 70

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                playerone.state = playerone.UPPERCUT
                playerone.punch.play()
            if event.key == pygame.K_LEFT:
                playerone.state = playerone.LEFTDODGE
                playerone.dodge.play()
            if event.key == pygame.K_RIGHT:
                playerone.state = playerone.RIGHTDODGE
                playerone.dodge.play()
            if event.key == pygame.K_a:
                playerone.state = playerone.LEFTBODYBLOW
                playerone.punch.play()
            if event.key == pygame.K_d:
                playerone.state = playerone.RIGHTBODYBLOW
                playerone.punch.play()
            if event.key == pygame.K_DOWN:
                playerone.state = playerone.DOWNDODGE
                playerone.dodge.play()
            if event.key == pygame.K_s:
                playerone.state = playerone.DOWNDUCK
                playerone.dodge.play()

            # checking if up modifier is pressed
            if event.key == pygame.K_LEFT & pygame.K_UP:
                playerone.state = playerone.LEFTFACEPUNCH
                playerone.punch.play()
            if event.key == pygame.K_RIGHT & pygame.K_UP:
                playerone.state = playerone.RIGHTFACEPUNCH
                playerone.punch.play()
    # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
    allSprites.clear(screen, background)
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
    timertext = font.render(output_string, True, white)
    screen.blit(timertext, [420, 38])
    hearts = "3"
    hearttext = font.render(hearts, True, white)
    screen.blit(hearttext, [120, 30])
    stars = "1"
    startext = font.render(stars, True, white)
    screen.blit(startext, [65, 30])
    gamescore = "1500"
    gamescoretext = font.render("Points:  "+str(gamescore), True, white)
    screen.blit(gamescoretext, [180, 47])
    #display stuff
    health_bars(player_health, opponent_health)
        # --- Timer going down ---
    # Blit to the screen
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    frame_count += 1
    # Limit to 20 frames per second
    clock.tick(frame_rate)
    allSprites.update()
    allSprites.draw(screen)
    pygame.display.flip()
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()

