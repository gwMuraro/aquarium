from utils.ObjetsSprite.SpriteBase import *

class SpriteIHM(SpriteBase) :
    
    def __init__(self, x=0, y=0, largeur=0, hauteur=0, chemin_image="") : 
        SpriteBase.__init__(self, x, y, largeur, hauteur, chemin_image)
        self.redimensionner(largeur, hauteur)
        
    def clique(self, context=None) :
        pass
    

