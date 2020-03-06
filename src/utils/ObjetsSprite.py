import pygame

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
        self.velocite = 3
    
    def deplacement(self) : 
        self.rect.x += self.velocite

    def redimensionner(self, largeur, hauteur) : 
        self.image = pygame.transform.scale(self.image, (largeur, hauteur))