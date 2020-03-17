import random
import sys
from utils.ObjetsSprite.SpriteVivant import *
import utils.FileReader.ConfigSingleton as cs



class ControlleurJeu() :
        
    #largeur_fenetre = 1000
    #hauteur_fenetre = 600
    #largeur_aquarium = 800
    #hauteur_aquarium = 600
    
    # Pattern singleton 
    __INSTANCE_CONTROLLEUR_JEU = None

    def __init__(self) : 

        config = cs.ConfigSingleton.getConfig()

        ControlleurJeu.largeur_fenetre = config["aquarium"]["affichage"]["largeur_fenetre"]
        self.largeur_fenetre = config["aquarium"]["affichage"]["largeur_fenetre"]
        
        ControlleurJeu.hauteur_fenetre = config["aquarium"]["affichage"]["hauteur_fenetre"]
        self.hauteur_fenetre = config["aquarium"]["affichage"]["hauteur_fenetre"]
        
        ControlleurJeu.largeur_aquarium = config["aquarium"]["affichage"]["largeur_aquarium"]
        self.largeur_aquarium = config["aquarium"]["affichage"]["largeur_aquarium"]
        
        ControlleurJeu.hauteur_aquarium = config["aquarium"]["affichage"]["hauteur_aquarium"]
        self.hauteur_aquarium = config["aquarium"]["affichage"]["hauteur_aquarium"]
        
        self.FPS = 30
        self.une_seconde = self.FPS * 1
        self.cpt_FPS = 0

        self.nombre_poissons = 10
        self.nombre_piranhas = 3 
        self.nombre_crevettes = 3
        self.cagnotte = 100000

        self.vivants = list()

        self.indice_poisson_actuel = None
        self.informations_poisson = " "

    def creationVivants(self) : 
        config = cs.ConfigSingleton.getConfig()
        for clef, valeur in config["aquarium"]["vivants"].items() : 
            for i in range(valeur): 
                x = random.randint(0, self.largeur_aquarium - 60)
                y = random.randint(0, self.hauteur_aquarium - 40)
                self.vivants.append(SpriteVivant(x, y, config[clef]["affichage"]["largeur"], config[clef]["affichage"]["hauteur"], type_poisson=clef))

    def tuerLePoisson(self, poisson): 
        # mise à jour de l'affichage des informations du poisson 
        if self.indice_poisson_actuel!= None and self.indice_poisson_actuel == self.vivants.index(poisson) : 
            # si le poisson actuel meurt 
            self.indice_poisson_actuel = None
            self.informations_poisson = ""
        elif self.indice_poisson_actuel!= None and self.indice_poisson_actuel > self.vivants.index(poisson) : 
            # si c'est un poisson de rang inférieur qui meurt 
            self.indice_poisson_actuel -= 1 
        
        SpriteBase.sTabTousLesSprites.remove(poisson)
        self.vivants.remove(poisson)
        
        # si on a juste eu un décalage dans la liste des poissons 
        if self.indice_poisson_actuel != None : 
            self.informations_poisson = self.vivants[self.indice_poisson_actuel].poisson.getInformations()

    # TODO : Pattern factory peut être ici
    def ajouteVivant(self, type_poisson="gupy") : 
        config = cs.ConfigSingleton.getConfig()
        x = random.randint(0, self.largeur_aquarium - config[type_poisson]["affichage"]["largeur"])
        y = random.randint(0, self.hauteur_aquarium - config[type_poisson]["affichage"]["hauteur"])
        self.vivants.append(SpriteVivant(x, y, config[type_poisson]["affichage"]["largeur"], config[type_poisson]["affichage"]["hauteur"], type_poisson=type_poisson))

    def actionsPeriodiques(self) : 

        # pour tous les vivants
        for vivant in self.vivants : 
            
            # GESTION DU DEPLACEMENT
            vivant.deplacement()

            # GESTION DE LA VISUALISATION DU POISSON 
            if self.indice_poisson_actuel != None : 
                self.informations_poisson = self.vivants[self.indice_poisson_actuel].poisson.getInformations()

            # GESTION DE LA PREDATION
            # On ne traite le cas que des poissons prédateurs et s'il a faim
            if vivant.poisson.estPredateur() and vivant.poisson.aFaim() : 
                
                # On vérifie une à une les interractions possible avec le poisson
                for i in range(len(self.vivants)-1, -1, -1) :  # TODO : utiliser un foreach plutot qu'un iterateur
                    
                    # Si le prédateur est en contact avec un Sprite 
                    if vivant.rect.colliderect(self.vivants[i].rect) : 
                        
                        # si le poisson en collision est une proie, on la mange 
                        if self.vivants[i].poisson.type_poisson in vivant.poisson.liste_proies : 
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
            
    def getControlleurJeu() : 
        if ControlleurJeu.__INSTANCE_CONTROLLEUR_JEU == None : 
            ControlleurJeu.__INSTANCE_CONTROLLEUR_JEU = ControlleurJeu()
            print("Création du controlleur du jeu")

        return ControlleurJeu.__INSTANCE_CONTROLLEUR_JEU