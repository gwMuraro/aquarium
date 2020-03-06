import pygame
import utils.Poisson as Poisson

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
        
class SpritePoisson(SpriteBase) : 
    
    def __init__(self, x, y, largeur, hauteur, chemin_image) :
        SpriteBase.__init__(self, x, y, largeur, hauteur, chemin_image)
        self.velocite = 5
        self.poisson = Poisson.Poisson(50, self.velocite)
    
    def deplacement(self) : 
        nouveau_x_y = self.poisson.calculDeplacement(self.rect.x, self.rect.y, self.rect.width, self.rect.height)
        self.rect.x += nouveau_x_y[0]
        self.rect.y += nouveau_x_y[1]
        

    def redimensionner(self, largeur, hauteur) : 
        self.image = pygame.transform.scale(self.image, (largeur, hauteur))
        self.rect.width = largeur
        self.rect.height = hauteur

    def setVelocite(self, velocite) : 
        self.velocite = velocite
        self.poisson.velocite = velocite
