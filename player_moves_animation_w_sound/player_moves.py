""" player_moves.py 
    illustrates a multi-frame animation
    Responding to input and adding state and sound
"""
import pygame
pygame.init()

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
        self.rect.center = (320, 240)
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


screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Testing Player Moves")

background = pygame.Surface(screen.get_size())
background.fill((0, 0x99, 0))
screen.blit(background, (0, 0))

playerone = Playerone()
allSprites = pygame.sprite.Group(playerone)

clock = pygame.time.Clock()
keepGoing = True

while keepGoing:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoing = False
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
    allSprites.clear(screen, background)
    allSprites.update()
    allSprites.draw(screen)
    pygame.display.flip()
