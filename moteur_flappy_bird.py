import pygame
import random
class Tuyeau(pygame.sprite.Sprite):
    def __init__(self, couple):
        super().__init__()
        x, y=couple
        self.image=pygame.Surface((80, 220))
        self.image.fill((0, 255, 0))
        self.rect=self.image.get_rect(center=(x, y))
        
    def update(self):
        self.rect.x-=10
        if self.rect.x==-200:
            self.rect.x=800
class Bird:
    def __init__(self):
        self.image=pygame.Surface((60, 60))
        self.image.fill((0, 0, 255))
        
        self.rect=self.image.get_rect(center=(400, 300))
    def update(self, liste_touche):
        self.rect.y+=8
        if liste_touche:
            self.rect.x=-100
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.verif=True
        self.image=pygame.Surface((20, 10))
        self.image.fill((255, 0, 0))
        
        self.rect=self.image.get_rect(center=(0, 0))
    def update(self, visible=False):
        self.rect.x-=8
        if  self.rect.x<=0:
            self.rect.x-=10
        if visible and self.verif:
            self.rect.x=600
            coordonnees_y=random.randint(160, 440)  
            self.rect.y=coordonnees_y
            self.verif=False
        