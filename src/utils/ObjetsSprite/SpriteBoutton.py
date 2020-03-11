from utils.ObjetsSprite.SpriteBase import *

class SpriteBoutton(SpriteBase) : 
    def __init__(self, x, y, largeur, hauteur, chemin_image) : 
        SpriteBase.__init__(self, x, y, largeur, hauteur, chemin_image)
        self.redimensionner(largeur, hauteur)
    
    def clique(self, contexte) :
        print("Clique sur ajouté")
        if contexte.cagnotte >= 50 : 
            contexte.cagnotte -= 50
            contexte.ajouteVivant()
    
    