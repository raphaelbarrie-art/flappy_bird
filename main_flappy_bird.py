import pygame
import sys
import random
from moteur_flappy_bird import Tuyeau, Bird, Obstacle
pygame.init()
longueur, largeur=(800, 600)
ecran=pygame.display.set_mode((longueur, largeur))
horloge=pygame.time.Clock()
obstacle=0
en_jeu=True
liste_position_tuyeau=[(800, 600), (600, 600), (400, 600), (200, 600), (0, 600), (800, 0), (600, 0), (400, 0), (200, 0), (0, 0)]
groupe_sprite=pygame.sprite.Group()
for i in range(10):
    groupe_sprite.add(Tuyeau(liste_position_tuyeau[i]))
gg=Obstacle()    
while en_jeu:
    evenement=pygame.event.get()
    for event in evenement:
        if event.type==pygame.QUIT:
            en_jeu=False
    groupe_sprite.update()
    if gg.rect.x<0:
        obstacle=random.randint(0,50)
    print(obstacle)
    if obstacle==14:
        gg.update(True)
    ecran.fill((0, 0, 0))
    
    groupe_sprite.draw(ecran)
    ecran.blit(gg.image, gg.rect)
    if obstacle==14  or gg.rect.x>0:
       print(obstacle)
    else:
        gg.verif=True
    pygame.display.flip()
    
    horloge.tick(30)
pygame.quit()
sys.exit()