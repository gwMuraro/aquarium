import pygame
import random
import sys
from utils.ObjetsSprite import *
from utils.DecorateurPredation import *


class ControlleurJeu() :
    
    def __init__(self) : 
        self.largeur_fenetre = 800
        self.hauteur_fenetre = 600
        
        self.FPS = 30
        self.une_seconde = self.FPS * 1
        self.cpt_FPS = 0

        self.nombre_poissons = 10
        self.nombre_piranhas = 3 
        self.cagnotte = 0

        self.vivants = list()

    def creationVivants(self) : 
        # création des poissons type gupys
        for i in range(self.nombre_poissons) : 
            x = random.randint(0, self.largeur_fenetre - 60)
            y = random.randint(0, self.hauteur_fenetre - 40)
            self.vivants.append(SpritePoisson(x, y, 60, 40, "src/images/poisson_vers_la_gauche.png"))
            self.vivants[i].poisson.inertie_max = 60
            self.vivants[i].poisson.velocite = random.randint(2, 4)

        # creation des poissons type piranhas
        for i in range(self.nombre_piranhas) : 
            x = random.randint(0, self.largeur_fenetre - 60)
            y = random.randint(0, self.hauteur_fenetre - 40)
            self.vivants.append(SpritePiranha(x, y, 60, 40, "src/images/poisson_vers_la_gauche.png"))
            self.vivants[len(self.vivants) - 1].devientPredateur()

    # TODO : Pattern factory peut être ici
    def ajouteVivant(self) : 
        x = random.randint(0, self.largeur_fenetre - 60)
        y = random.randint(0, self.hauteur_fenetre - 40)
        self.vivants.append(SpritePoisson(x, y, 60, 40, "src/images/poisson_vers_la_gauche.png"))

    def actionsPeriodiques(self) : 

        # pour tous les vivants
        for vivant in self.vivants : 
            
            # GESTION DU DEPLACEMENT
            vivant.deplacement()
            
            # GESTION DE LA PREDATION
            
            if vivant.poisson.estPredateur() : # on ne traite le cas que des poissons prédateurs
                
                # On vérifie une à une les interractions possible avec le poisson
                for i in range(len(self.vivants)-1, -1, -1) : 
                    
                    # Si le prédateur est en contact avec un Sprite 
                    if vivant.rect.colliderect(self.vivants[i].rect) : 
                        # si le poisson en collision est une proie, on la mange 
                        if self.vivants[i].poisson.estProie() : 
                            SpriteBase.sTabTousLesSprites.remove(self.vivants[i])
                            self.vivants.remove(self.vivants[i])

        # GESTION DE L'ECONOMIE EN FONCTION DES SECONDES
        if self.cpt_FPS % self.FPS == 0 :
            for vivant in self.vivants : 
                self.cagnotte += vivant.poisson.generationArgent()
        
        # GESTION DE L'HORLOGE
        self.cpt_FPS += 1
        if self.cpt_FPS == self.FPS : 
            self.cpt_FPS = 0

    def gestionEvenements(self, events) : 
        for event in events :
            
            if event.type == pygame.QUIT : 
                print("Nous quittons notre aquarium")
                pygame.quit()
                sys.exit(0)

            if event.type == pygame.MOUSEBUTTONDOWN : 
                # récupération de la position souris
                position = pygame.mouse.get_pos()

                # récupération des sprites en dessous de la souris 
                sprites_cliquees = [x for x in SpriteBase.sTabTousLesSprites if x.rect.collidepoint(position)]
                if len(sprites_cliquees) > 0 : 
                    # TODO : Peut être un observer à mettre ici
                    # Action de la sprite cliquée
                    sprites_cliquees[0].clique(self)
