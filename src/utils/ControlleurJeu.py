import pygame
import random
import sys

from utils.DecorateurPredation import *
from utils.ObjetsSprite import ObjetsSprite


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
            self.vivants.append(SpritePoisson(x, y, 60, 40))
            self.vivants[i].poisson.inertie_max = 60
            self.vivants[i].poisson.velocite = random.randint(2, 4)

        # creation des poissons type piranhas
        for i in range(self.nombre_piranhas) : 
            x = random.randint(0, self.largeur_fenetre - 60)
            y = random.randint(0, self.hauteur_fenetre - 40)
            self.vivants.append(SpritePiranha(x, y, 60, 40))
            self.vivants[len(self.vivants) - 1].devientPredateur()

    def tuerLePoisson(self, poisson): 
        SpriteBase.sTabTousLesSprites.remove(poisson)
        self.vivants.remove(poisson)

    # TODO : Pattern factory peut être ici
    def ajouteVivant(self) : 
        x = random.randint(0, self.largeur_fenetre - 60)
        y = random.randint(0, self.hauteur_fenetre - 40)
        self.vivants.append(SpritePoisson(x, y, 60, 40))

    def actionsPeriodiques(self) : 

        # pour tous les vivants
        for vivant in self.vivants : 
            
            # GESTION DU DEPLACEMENT
            vivant.deplacement()

            # GESTION DE LA PREDATION
            # on ne traite le cas que des poissons prédateurs et s'il a faim
            if vivant.poisson.estPredateur() and vivant.poisson.aFaim() : 
                
                # On vérifie une à une les interractions possible avec le poisson
                for i in range(len(self.vivants)-1, -1, -1) :  # TODO : utiliser un foreach plutot qu'un iterateur
                    # Si le prédateur est en contact avec un Sprite 
                    if vivant.rect.colliderect(self.vivants[i].rect) : 
                        # si le poisson en collision est une proie, on la mange 
                        if self.vivants[i].poisson.estProie() : 
                            vivant.poisson.mange(self.vivants[i].poisson.valeur_nutritive)
                            self.tuerLePoisson(self.vivants[i])
                            

        # GESTION EN FONCTION DES SECONDES
        if self.cpt_FPS % self.FPS == 0 :
            
            for vivant in self.vivants : 
                # GESTION DE L'ECONOMIE 
                self.cagnotte += vivant.poisson.generationArgent()

                # GESTION DE LA FAIM
                vivant.poisson.faim -= 1
                if vivant.poisson.faim <= 0 : 
                    self.tuerLePoisson(vivant)

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
