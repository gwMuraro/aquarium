import pygame
import utils.CoefDirection as cd
import utils.ControlleurJeu as ControlleurJeu
import utils.ObjetsSprite.SpriteBoutton as sb
import utils.ObjetsSprite.SpriteBase as sbase

if __name__ == "__main__":
        
    # initialisation du framework
    pygame.init()
    police = pygame.font.SysFont("ubuntu", 15)

    # Création du controlleur 
    controlleur = ControlleurJeu.ControlleurJeu()

    # --- Fenêtre 
    fenetre = pygame.display.set_mode((controlleur.largeur_fenetre, controlleur.hauteur_fenetre))
    pygame.display.set_caption("Aquarium")
    # Ajout d'un fond d'écran 
    fond = pygame.image.load("images/fond.jpg") # 1200 x 800
    # Fenêtre ---

    # --- Horloge
    # L'utilisation des images par secondes nous permettent de déterminer les secondes dans la mainloop
    horloge = pygame.time.Clock()
    # Horloge ---

    # --- Création de l'IHM
    
    bouton_plus_gupy = sb.SpriteBouttonAjouter(x=690, y=542, largeur=100, hauteur=48, chemin_image="images/bouton_ajouter.png", contexte=controlleur, type="gupy")
    bouton_plus_piranha = sb.SpriteBouttonAjouter(x=690, y=400, largeur=100, hauteur=48, chemin_image="images/bouton_ajouter.png", contexte=controlleur, type="piranha")
    # Création de l'IHM ---

    # --- Création des poissons
    controlleur.creationVivants()
    # Création des poissons ---

    # ========== MAIN LOOP =========
    bContinue = True
    while bContinue : 
        pygame.time.delay(10)

        # GESTION EVENNEMENT + MOUVEMENT + PREDATION + ECONOMIE
        controlleur.gestionEvenements(pygame.event.get())
        controlleur.actionsPeriodiques()

        # --- DESSIN 
        fenetre.fill((0,0,0))
        fenetre.blit(fond, (-200, -100)) # centrage par le calcul de la translation à faire
        
        # affichage de la cagnotte 
        libelle = police.render("Cagnotte : " + str(controlleur.cagnotte), 1, (255, 255, 0)) 
        fenetre.blit(libelle, (10, 10))
        
        # affichage des sprites 
        sbase.SpriteBase.sTabTousLesSprites.draw(fenetre) 
        
        pygame.display.flip()
        # DESSIN ---

        # --- HORLOGE
        horloge.tick(controlleur.FPS)
        # HORLOGE ---

