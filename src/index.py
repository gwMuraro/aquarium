import pygame, sys, random
from utils.ObjetsSprite import *
from utils.Direction import *

pygame.init()

# --- Fenêtre 
largeur_fenetre, hauteur_fenetre = 800, 600
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Aquarium")
# Ajout d'un fond d'écran 
fond = pygame.image.load("src/images/fond.jpg")
# Fenêtre ---

# --- Horloge
# L'utilisation des images par secondes nous permettent de déterminer 
# les secondes dans la mainloop
horloge = pygame.time.Clock()
FPS = 30
# Horloge ---

# --- Création des poissons
# un petit test de la classe des poissons
nb_poissons = 10
poissons = list()
for i in range(nb_poissons) : 
    x = random.randint(0, largeur_fenetre - 60)
    y = random.randint(0, hauteur_fenetre - 40)
    poissons.append(SpritePoisson(x, y, 60, 40, "src/images/fish.png"))
    poissons[i].redimensionner(60,40)
# Création des poissons ---


# ========== MAIN LOOP =========
bContinue = True
while bContinue : 
    pygame.time.delay(100)

    # --- Evenements 
    for event in pygame.event.get() :
        if event.type == pygame.QUIT : 
            bContinue = False
    # Evenements ---

    # --- Mouvement
    for poisson in poissons : 
        poisson.deplacement()
    # Mouvement --- 

    # --- Dessin 
    fenetre.fill((0,0,0))
    fenetre.blit(fond, (0,0))
    SpriteBase.sTabTousLesSprites.draw(fenetre)
    pygame.display.flip()
    # Dessin ---

    # --- Horloge
    horloge.tick(FPS)
    # Horloge ---




print("Nous quittons notre aquarium")

pygame.quit()