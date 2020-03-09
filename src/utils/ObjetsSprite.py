import pygame
from utils.Direction import *
from utils.Poisson import *
from utils.DecorateurPredation import *
#from utils.ControlleurJeu import *

class SpriteBase(pygame.sprite.Sprite) : 
    
    # Grâce à ce tableau, on va pouvoir actualiser tous les sprites en une action
    sTabTousLesSprites = pygame.sprite.Group() 

    def __init__(self, x, y, largeur, hauteur, chemin_image) :

        # Chargement de la super classe
        pygame.sprite.Sprite.__init__(self)

        # Ajout du sprite dans la liste de tous les sprites
        SpriteBase.sTabTousLesSprites.add(self)

        self.image = pygame.image.load(chemin_image) # image de notre sprite
        self.rect = self.image.get_rect()  # box de notre sprite
        
        # Origine de l'image dans le plan 
        self.rect.x = x
        self.rect.y = y

        # Dimension de l'image
        self.width = largeur 
        self.height = hauteur
    
    def redimensionner(self, largeur, hauteur) : 
        self.image = pygame.transform.scale(self.image, (largeur, hauteur))
        self.rect.width = largeur
        self.rect.height = hauteur

    def clique(self, contexte) :
        print("clique sur un sprite sans comportement")

class SpritePoisson(SpriteBase) : 
    
    DIRECTIONS_DROITE = [1, 2, 3]
    DIRECTIONS_GAUCHE = [5, 6, 7]
    CHEMIN_POISSON_VERS_GAUCHE = "src/images/poisson_vers_la_gauche.png"
    CHEMIN_POISSON_VERS_DROITE = "src/images/poisson_vers_la_droite.png"

    def __init__(self, x, y, largeur, hauteur, chemin_image) :
        SpriteBase.__init__(self, x, y, largeur, hauteur, chemin_image)
        self.velocite = 5
        self.poisson = DecorationProie(Poisson(50, self.velocite))
        self.redimensionner(largeur, hauteur)
        self.transposition()
    
    def deplacement(self) : 
        # Ancienne direction 
        ancienne_direction = self.poisson.coef_direction[2]

        # Calcul du nouveau positionnement sur l'écran 
        nouveau_x_y = self.poisson.calculDeplacement(self.rect.x, self.rect.y, self.rect.width, self.rect.height)

        # Positionnement 
        self.rect.x += nouveau_x_y[0]
        self.rect.y += nouveau_x_y[1]

        # ---- TODO : Optimiser ce systeme de Vérification de direction 
        # Nouvelle direction 
        nouvelle_direction = self.poisson.coef_direction[2]

        # Transposition verticale si besoin 
        if ancienne_direction != nouvelle_direction : 
            self.transposition()
        # ----
        
    def setVelocite(self, velocite) : 
        self.velocite = velocite
        self.poisson.velocite = velocite

    def transposition(self) : 
        # Choix de la bonne sprite 
        if self.poisson.coef_direction[2] in SpritePoisson.DIRECTIONS_DROITE : 
            self.image = pygame.image.load(SpritePoisson.CHEMIN_POISSON_VERS_DROITE)
        if self.poisson.coef_direction[2] in SpritePoisson.DIRECTIONS_GAUCHE : 
            self.image = pygame.image.load(SpritePoisson.CHEMIN_POISSON_VERS_GAUCHE)
        
        # redimensionnement de la nouvelle image 
        self.redimensionner(self.rect.width, self.rect.height)

class SpritePiranha(SpriteBase) :
    
    DIRECTIONS_DROITE = [1, 2, 3]
    DIRECTIONS_GAUCHE = [5, 6, 7]
    CHEMIN_PIRANHA_VERS_GAUCHE = "src/images/piranha.jpg"
    CHEMIN_PIRANHA_VERS_DROITE = "src/images/piranha.jpg"

    def __init__(self, x, y, largeur, hauteur, chemin_image) :
        SpriteBase.__init__(self, x, y, largeur, hauteur, SpritePiranha.CHEMIN_PIRANHA_VERS_DROITE)
        self.velocite = 5
        self.poisson = Poisson(50, self.velocite)
        self.redimensionner(largeur, hauteur)

    def deplacement(self) : 
        # Ancienne direction 
        ancienne_direction = self.poisson.coef_direction[2]

        # Calcul du nouveau positionnement sur l'écran 
        nouveau_x_y = self.poisson.calculDeplacement(self.rect.x, self.rect.y, self.rect.width, self.rect.height)

        # Positionnement 
        self.rect.x += nouveau_x_y[0]
        self.rect.y += nouveau_x_y[1]

        # ---- TODO : Optimiser ce systeme de Vérification de direction 
        # Nouvelle direction 
        nouvelle_direction = self.poisson.coef_direction[2]

        # Transposition verticale si besoin 
        # if ancienne_direction != nouvelle_direction : 
        #     self.transposition()
        # ----
    
    def setVelocite(self, velocite) : 
        self.velocite = velocite
        self.poisson.velocite = velocite
    
    def devientPredateur(self) : 
        if type(self.poisson).__name__ != DecorationPredateur.__name__ :
            self.poisson = DecorationPredateur(self.poisson)
            print("DEBUG : Je devient prédateur") 

class SpriteBoutton(SpriteBase) : 
    def __init__(self, x, y, largeur, hauteur, chemin_image) : 
        SpriteBase.__init__(self, x, y, largeur, hauteur, chemin_image)
        self.redimensionner(largeur, hauteur)
    
    def clique(self, contexte) :
        print("Clique sur ajouté")
        if contexte.cagnotte >= 50 : 
            contexte.cagnotte -= 50
            contexte.ajouteVivant()
        