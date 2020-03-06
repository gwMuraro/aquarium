import pygame
from utils.ObjetsSprite import *

pygame.init()

# --- Fenêtre 
largeur, hauteur = 800, 600
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Aquarium")
# Fenêtre ---

# --- Horloge
# L'utilisation des images par secondes nous permettent de déterminer 
# les secondes dans la mainloop
horloge = pygame.time.Clock()
FPS = 24 
# Horloge ---

# --- Image
# un petit test de la classe des poissons
poisson = SpritePoisson(0,100, 60, 40, "src/images/fish.png")
poisson.redimensionner(60,40)
# Image ---


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
    poisson.deplacement()
    # Mouvement --- 

    # --- Dessin 
    fenetre.fill((0,0,0))
    SpriteBase.sTabTousLesSprites.draw(fenetre)
    pygame.display.flip()
    # Dessin ---

    # --- Horloge
    horloge.tick(FPS)
    # Horloge ---




print("Nous quittons notre aquarium")

pygame.quit()