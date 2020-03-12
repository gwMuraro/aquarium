from utils.ObjetsSprite.SpriteBase import *


class SpriteBoutton(SpriteBase) : 
    def __init__(self, x=0, y=0, largeur=0, hauteur=0, chemin_image="") : 
        SpriteBase.__init__(self, x, y, largeur, hauteur, chemin_image)
        self.redimensionner(largeur, hauteur)
    
    def clique(self, contexte) :
        print("clic sur ajouté")
        if contexte.cagnotte >= 50 : 
            contexte.cagnotte -= 50
            contexte.ajouteVivant()
    
    