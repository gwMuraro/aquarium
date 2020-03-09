import pygame
import random
from utils.ObjetsSprite import *
from utils.DecorateurPredation import *
from utils.ControlleurJeu import * 
#from utils.Direction import *


# initialisation du framework
pygame.init()
police = pygame.font.SysFont("ubuntu", 15)

# Création du controlleur 
controlleur = ControlleurJeu()

# --- Fenêtre 
fenetre = pygame.display.set_mode((controlleur.largeur_fenetre, controlleur.hauteur_fenetre))
pygame.display.set_caption("Aquarium")
# Ajout d'un fond d'écran 
fond = pygame.image.load("src/images/fond.jpg") # 1200 x 800
# Fenêtre ---

# --- Horloge
# L'utilisation des images par secondes nous permettent de déterminer les secondes dans la mainloop
horloge = pygame.time.Clock()
FPS = 30
une_seconde = FPS 
cpt_FPS = 0
# Horloge ---

# --- Création de l'IHM
bouton_plus = SpriteBoutton(690, 542, 100, 48, "src/images/bouton_ajouter.png")
# Création de l'IHM ---

# --- Création des poissons
controlleur.creationVivants()
# Création des poissons ---

# ========== MAIN LOOP =========
bContinue = True
while bContinue : 
    pygame.time.delay(10)

    # --- Evenements pygame
    for event in pygame.event.get() :
        if event.type == pygame.QUIT : 
            bContinue = False
        if event.type == pygame.MOUSEBUTTONDOWN : 
            # récupération de la position souris
            position = pygame.mouse.get_pos()

            # récupération des sprites en dessous de la souris 
            sprites_cliquees = [x for x in SpriteBase.sTabTousLesSprites if x.rect.collidepoint(position)]
            if len(sprites_cliquees) > 0 : 
                # Action de la sprite cliquée
                sprites_cliquees[0].clique()
    # Evenements pygame ---

    controlleur.actionsPeriodiques()
   
    # # --- Cagnotte 
    # if cpt_FPS % une_seconde == 0 : 
    #     for vivant in poissons + piranhas : 
    #         cagnotte += vivant.poisson.generationArgent()
            
    # Cagnotte ---

    # --- Dessin 
    fenetre.fill((0,0,0))
    # calcul de translation pour x : 0 - ((largeur_image - largeur_fenetre) / 2)
    # calcul de translation pour y : 0 - ((hauteur_image - hauteur_fenetre) / 2)
    fenetre.blit(fond, (-200, -100)) # centrage par le calcul de la translation à faire
    
    # affichage de la cagnotte 
    libelle = police.render("Cagnotte : " + str(controlleur.cagnotte), 1, (255, 255, 0)) 
    fenetre.blit(libelle, (10, 10))
    
    # affichage des sprites 
    SpriteBase.sTabTousLesSprites.draw(fenetre) 
    
    pygame.display.flip()
    # Dessin ---

    # --- Horloge
    horloge.tick(FPS)
    # Horloge ---

print("Nous quittons notre aquarium")

pygame.quit()