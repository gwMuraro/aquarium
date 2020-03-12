from utils.ObjetsSprite.SpriteBase import *
from utils.ObjetsSprite.CallBacks import *

class SpriteBoutton(SpriteBase) : 
    
    def __init__(self, x=0, y=0, largeur=0, hauteur=0, chemin_image="") : 
        SpriteBase.__init__(self, x, y, largeur, hauteur, chemin_image)
        self.redimensionner(largeur, hauteur)
        
    def clique(self, contexte) :
        pass

class SpriteBouttonAjouter(SpriteBoutton) : 

    def __init__(self, x, y, largeur, hauteur, chemin_image, contexte, type) : 
        SpriteBoutton.__init__(self, x, y, largeur, hauteur, chemin_image)
        self.type = type 
        self.contexte = contexte
        
    def clique(self, contexte) : 
        if contexte.cagnotte > 50 :
            contexte.cagnotte -= 50 
            contexte.ajouteVivant(type_poisson = self.type)
        

