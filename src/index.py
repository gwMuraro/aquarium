import pygame

pygame.init()

# === Fenêtre 
largeur, hauteur = 800, 600
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Aquarium")
# Fenêtre ===

# === Image
image_poisson = pygame.image.load("src/images/fish.png")
image_poisson = pygame.transform.scale(image_poisson, (60, 40))
# Image ===

# ========== MAIN LOOP =========
bContinue = True
while bContinue : 
    pygame.time.delay(100)

    # === Evenements 
    for event in pygame.event.get() :
        if event.type == pygame.QUIT : 
            bContinue = False
    # Evenements ===

    # === Dessin 
    fenetre.blit(image_poisson, (200, 200)) # dessine le poisson
    pygame.display.flip()
    # Dessin ===
print("Nous quittons notre aquarium")

pygame.quit()