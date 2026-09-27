import pygame
import sys
import random
from moteur_flappy_bird import Tuyeau, Bird, Obstacle
pygame.init()
longueur, largeur=(800, 600)
ecran=pygame.display.set_mode((longueur, largeur))
horloge=pygame.time.Clock()
obstacle=0
score=0
vitesse=8
lose=False
font=pygame.font.SysFont("Arial", 25, bold=True)
en_jeu=True
liste_position_tuyeau=[(800, 600), (600, 600), (400, 600), (200, 600), (0, 600), (800, 0), (600, 0), (400, 0), (200, 0), (0, 0)]
groupe_sprite=pygame.sprite.Group()
for i in range(10):
    groupe_sprite.add(Tuyeau(liste_position_tuyeau[i]))
ennemi=Obstacle()
personnage=Bird()
text_end=font.render("Game OVER appuyer sur r pour restart", False, (255, 0, 0))
rect_text_end=text_end.get_rect(center=(-30,-50))
while en_jeu:
    test_score=score/500
    if test_score==1:
        vitesse+=9
    elif test_score==1.5:
        vitesse+=10
    elif test_score==2:
        vitesse+=15
    elif test_score==3:
        vitesse+=30
    score+=1
    evenement=pygame.event.get()
    for event in evenement:
        if event.type==pygame.QUIT:
            en_jeu=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_r:
                score=0
                lose=False
                vitesse=8
                obstacle=0
                personnage.reset()
                ennemi.reset()
    text=font.render(f"score:{score} ", True, (255, 255, 255))
    rect_text=text.get_rect(topleft=(0, 0))
    
    groupe_sprite.update()
    if ennemi.rect.x<=0:
        if 0<= test_score< 0.99:
            obstacle=random.randint(0,50)
        elif 1<= test_score<=2.5:
            obstacle=random.randint(0, 25)
        elif 2.5<= test_score<=3:
            obstacle=random.randint(10, 22)
        elif obstacle>3.1:
            obstacle=random.randint(13, 14)
    if obstacle==14:
        ennemi.update(True, vitesse)
        if ennemi.rect.x<=0:
            ennemi.rect.x-=10
    liste_touche=pygame.sprite.spritecollide(personnage, groupe_sprite, False)
    personnage.update(liste_touche, evenement, sys.modules[__name__])
    ecran.fill((0, 0, 0))
    if lose==False:    
        groupe_sprite.draw(ecran)
        ecran.blit(ennemi.image, ennemi.rect)
        ecran.blit(personnage.image, personnage.rect)
        ecran.blit(text, rect_text)
    elif lose:
        ecran.blit(text_end, rect_text_end)
        
    if obstacle==14  or ennemi.rect.x>0:
      v_sert_a_rien=2
    else:
        ennemi.verif=True
    pygame.display.flip()
    
    horloge.tick(30)
pygame.quit()
sys.exit()