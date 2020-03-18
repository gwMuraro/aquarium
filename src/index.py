import pygame
from pygame.locals import *
import utils.CoefDirection as cd
import utils.ControlleurJeu as cj
import utils.ObjetsSprite.SpriteBoutton as sb
import utils.ObjetsSprite.SpriteBase as sbase
import utils.ObjetsSprite.SpriteIHM as si
import utils.FileReader.ConfigSingleton as cs
import utils.Fenetre as Fenetre

config = cs.ConfigSingleton.getConfig()

if __name__ == "__main__":
    #initialisation du framework
    pygame.init()
    police = pygame.font.SysFont("ubuntu", 15)
    config = cs.ConfigSingleton.getConfig()

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

    # TODO : mettre les calculs de ratios en objets pour plus tard
    def calcul_ihm(valeur_en_pourcent, valeur_reference = config["aquarium"]["affichage"]["largeur_fenetre"]) : 
        return int((int(valeur_en_pourcent.split("%")[0]) * valeur_reference) / 100)

    largeur_ref = config["aquarium"]["affichage"]["largeur_fenetre"]
    hauteur_ref = config["aquarium"]["affichage"]["hauteur_fenetre"]
    
    separation_ihm = si.SpriteIHM(\
        x = calcul_ihm(config["ihm"]["panneau_lateral"]["x"]), \
        y = calcul_ihm(config["ihm"]["panneau_lateral"]["y"]), \
        largeur = calcul_ihm(config["ihm"]["panneau_lateral"]["largeur"]), \
        hauteur = calcul_ihm(config["ihm"]["panneau_lateral"]["hauteur"], hauteur_ref), \
        chemin_image = config["ihm"]["panneau_lateral"]["chemin_image"])
    
    cadre_info = si.SpriteIHM(\
        x = calcul_ihm(config["ihm"]["cadre_info"]["x"]), \
        y = calcul_ihm(config["ihm"]["cadre_info"]["y"]), \
        largeur = calcul_ihm(config["ihm"]["cadre_info"]["largeur"]), \
        hauteur = calcul_ihm(config["ihm"]["cadre_info"]["hauteur"], hauteur_ref), \
        chemin_image = config["ihm"]["cadre_info"]["chemin_image"])

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
        #fenetre.blit(fond, (0,0)) # centrage par le calcul de la translation à faire
        # pygame.display.flip()
        
        sbase.SpriteBase.sTabTousLesSprites.draw(fenetre) 

        # affichage de la cagnotte 
        libelle = police.render("Cagnotte : " + str(controlleur.cagnotte), 1, (255, 255, 0)) 
        fenetre.blit(libelle,(10, 10))
        
        # affichage des infos du poisson
        info_poisson = controlleur.informations_poisson
        blank = calcul_ihm("3%", hauteur_ref)
        for line in info_poisson.splitlines() : 
            blank += calcul_ihm("3%", hauteur_ref)
            lib = police.render(line, 1, (0, 0, 0))
            fenetre.blit(lib, (controlleur.largeur_aquarium + calcul_ihm("3%"), blank))

        
        # affichage des sprites 
        
        pygame.display.flip()
        
        # DESSIN ---

        # --- HORLOGE
        horloge.tick(controlleur.FPS)
        # HORLOGE ---
