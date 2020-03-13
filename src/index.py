import pygame
import utils.CoefDirection as cd
import utils.ControlleurJeu as ControlleurJeu
import utils.ObjetsSprite.SpriteBoutton as sb
import utils.ObjetsSprite.SpriteBase as sbase
import utils.FileReader.ConfigSingleton as cs


data = cs.ConfigSingleton.getConfig()
#print({SpriteBouttonAjouter()})


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

    # --- Création de l'IHM
    # TODO : changer les carrés en images 
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
    #bouton_plus_gupy = sb.SpriteBouttonAjouter(x=controlleur.largeur_aquarium + 10, y=540, largeur=100, hauteur=50, chemin_image="images/poisson_vers_la_gauche.png", contexte=controlleur, type="gupy")
    #bouton_plus_piranha = sb.SpriteBouttonAjouter(x=controlleur.largeur_aquarium + 10, y=470, largeur=100, hauteur=50, chemin_image="images/piranha_vers_la_gauche.png", contexte=controlleur, type="piranha")
    #bouton_plus_crevette = sb.SpriteBouttonAjouter(x=controlleur.largeur_aquarium + 10, y=420, largeur=100, hauteur=50, chemin_image="images/crevette_vers_la_gauche.png", contexte=controlleur, type="crevette")
    bouton_plus_gupy = sb.SpriteBouttonAjouter(contexte=controlleur, tabDonnee="buton_ajout_gupy")
    bouton_plus_piranha = sb.SpriteBouttonAjouter(contexte=controlleur, tabDonnee="buton_ajout_piranha")
    bouton_plus_crevette  = sb.SpriteBouttonAjouter(contexte=controlleur, tabDonnee="bouton_ajout_crevette")
    bouton_plus_meduse  = sb.SpriteBouttonAjouter(contexte=controlleur, tabDonnee="bouton_ajout_meduse")

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
        fenetre.fill((0,0,0))
        fenetre.blit(fond, (0,0)) # centrage par le calcul de la translation à faire
        
        # affichage de la cagnotte 
        libelle = police.render("Cagnotte : " + str(controlleur.cagnotte), 1, (255, 255, 0)) 
        fenetre.blit(libelle, (10, 10))
        
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

