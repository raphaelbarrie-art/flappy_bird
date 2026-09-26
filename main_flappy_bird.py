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
ennemi=Obstacle()
personnage=Bird()
while en_jeu:
    evenement=pygame.event.get()
    for event in evenement:
        if event.type==pygame.QUIT:
            en_jeu=False
    groupe_sprite.update()
    if ennemi.rect.x<=0:
        obstacle=random.randint(0,50)
    if obstacle==14:
        ennemi.update(True)
        if ennemi.rect.x<=0:
            ennemi.rect.x-=10
    liste_touche=pygame.sprite.spritecollide(personnage, groupe_sprite, False)
    personnage.update(liste_touche)
    ecran.fill((0, 0, 0))
    groupe_sprite.draw(ecran)
    ecran.blit(ennemi.image, ennemi.rect)
    ecran.blit(personnage.image, personnage.rect)
    if obstacle==14  or ennemi.rect.x>0:
      v_sert_a_rien=2
    else:
        ennemi.verif=True
    pygame.display.flip()
    
    horloge.tick(30)
pygame.quit()
sys.exit()