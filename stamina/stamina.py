import pygame
import math

class PlayerStaminaBar(object):
    def __init__(self, screen, image_source, location):
        self.screen   = screen
        self.image    = pyg.image.load(image_source)
        self.location = location
        
        self.top_left     = (175, 30)
        self.top_right    = (275, 30)
        self.bottom_left  = (175, 45)
        self.bottom_right = (275, 45)
        self.height       = abs(self.top_left[1] - self.bottom_left[1])
        self.width        = abs(self.top_left[0] - self.top_right[0])
        self.color        = (0, 255, 0)
        
        self.max_stamina   = self.width
        self.stamina       = 0
        
    def increase_stamina(self, amount):
        self.stamina += amount
        if self.stamina > self.max_stamina:
            self.stamina = self.max_stamina
        
    def decrease_stamina(self, amount):
        self.stamina -= amount
        if self.stamina < 0:
            self.stamina = 0
            
    def is_knockeddown(self):
        return self.stamina == 0
        
    def is_full_stamina(self):
        return self.stamina >= self.max_stamina
        
    def full_stamina(self):
        self.stamina = self.max_stamina
        
    def zero_stamina(self):
        self.stamina = 0
        
    def display(self):
        # first draw our image.
        self.screen.blit(self.image, (self.location.x, self.location.y))
        # build our rectangle but only if we still have stamina.
        if not self.is_dead():
            bar = pygame.Rect(self.top_left[0], 
                           self.top_left[1], 
                           self.stamina, # now we draw it only as long as stamina.
                           self.height)
                       
            # draw our rectangle on top of the image
            # 0 width means fill rectangle.
            pygame.draw.rect(self.screen, self.color, bar, 0)

class OpponentStaminaBar(object):
    def __init__(self, screen, image_source, location):
        self.screen   = screen
        self.image    = pyg.image.load(image_source)
        self.location = location
        
        self.top_left     = (290, 30)
        self.top_right    = (390, 30)
        self.bottom_left  = (290, 45)
        self.bottom_right = (390, 45)
        self.height       = abs(self.top_left[1] - self.bottom_left[1])
        self.width        = abs(self.top_left[0] - self.top_right[0])
        self.color        = (0, 255, 0)
        
        self.max_stamina   = self.width
        self.stamina       = 0
        
    def increase_stamina(self, amount):
        self.stamina += amount
        if self.stamina > self.max_stamina:
            self.stamina = self.max_stamina
        
    def decrease_stamina(self, amount):
        self.stamina -= amount
        if self.stamina < 0:
            self.stamina = 0
            
    def is_knockeddown(self):
        return self.stamina == 0
        
    def is_full_stamina(self):
        return self.stamina >= self.max_stamina
        
    def full_stamina(self):
        self.stamina = self.max_stamina
        
    def zero_stamina(self):
        self.stamina = 0
        
    def display(self):
        # first draw our image.
        self.screen.blit(self.image, (self.location.x, self.location.y))
        # build our rectangle but only if we still have stamina.
        if not self.is_knockeddown():
            bar = pygame.Rect(self.top_left[0], 
                           self.top_left[1], 
                           self.stamina, # now we draw it only as long as stamina.
                           self.height)
                       
            # draw our rectangle on top of the image
            # 0 width means fill rectangle.
            pygame.draw.rect(self.screen, self.color, bar, 0)
        
