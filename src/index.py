import pygame
#from pygame.locals import *
import utils.ControlleurJeu as cj
import utils.ObjetsSprite.SpriteBoutton as sb
import utils.ObjetsSprite.SpriteBase as sbase
import utils.FileReader.ConfigSingleton as cs

import utils.Fenetre as Fenetre

config = cs.ConfigSingleton.getConfig()

if __name__ == "__main__":
    #initialisation du framework
    pygame.init()
    police = pygame.font.SysFont("ubuntu", 15)
    

    # Création du controlleur 
    controlleur = cj.ControlleurJeu.getControlleurJeu()

    # --- Fenêtre 

    # Ajout d'un fond d'écran 
    fenetre = Fenetre.Fenetre()
    fond=config["fond_fenetre"]["chemin"]
    tailleFenetre = (config["aquarium"]["affichage"]["largeur_fenetre"] , config["aquarium"]["affichage"]["hauteur_fenetre"])
    fond = fenetre.creationFenetre(tailleFenetre,fond)
   
    
    # Fenêtre --- 

    # --- Création de l'IHM
    # Ajout d'un cadre pour le menu
    separation_ihm = pygame.draw.rect(fond, \
        (200, 180, 255), \
        (controlleur.largeur_aquarium, \
        0, \
        controlleur.largeur_fenetre - controlleur.largeur_aquarium, \
        controlleur.hauteur_fenetre))

    # Ajout des labels de visualisation 
    cadre_visu_informations = pygame.draw.rect(\
        fond, \
        (0,0,0), \
        (controlleur.largeur_aquarium + 10, \
        10, \
        controlleur.largeur_fenetre - (controlleur.largeur_aquarium + 20), \
        controlleur.hauteur_fenetre / 2))

    # Ajout des boutons d'ajout de vivants
    liste_boutons = list()
    for bouton in config["boutons_ajout"].keys() :
        liste_boutons.append(sb.SpriteBouttonAjouter(contexte=controlleur, tabDonnee=bouton))

    #  Création de l'IHM ---

    # --- Horloge
    # L'utilisation des images par secondes nous permettent de déterminer les secondes dans la mainloop
    horloge = pygame.time.Clock()
    # Horloge ---

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

        fenetre.redimension(fond)
        fenetre.fill((0,0,0))
        fenetre.blit(fond, (0,0))
        pygame.display.flip()

        
        # affichage de la cagnotte 
        libelle = police.render("Cagnotte : " + str(controlleur.cagnotte), 1, (255, 255, 0)) 
        fenetre.blit(libelle,(10, 10))
        
        # affichage des infos du poisson
        info_poisson = controlleur.informations_poisson
        blank = 0
        for line in info_poisson.splitlines() : 
            blank += 20
            lib = police.render(line, 1, (255, 255, 255))
            fenetre.blit(lib, (controlleur.largeur_aquarium + 20, blank))

        
        # affichage des sprites 
        sbase.SpriteBase.sTabTousLesSprites.draw(fenetre) 
        pygame.display.flip()
        
        # DESSIN ---

        # --- HORLOGE
        horloge.tick(controlleur.FPS)
        # HORLOGE ---
