from utils.ObjetsSprite.SpriteBase import *
from utils.ObjetsSprite.CallBacks import *
import utils.FileReader.ConfigSingleton as cs 
class SpriteBoutton(SpriteBase) : 
    
    def __init__(self, x=0, y=0, largeur=0, hauteur=0, chemin_image="") : 
        SpriteBase.__init__(self, x, y, largeur, hauteur, chemin_image)
        self.redimensionner(largeur, hauteur)
        
    def clique(self) :
        pass

    def clicable(self) : 
        return True

class SpriteBouttonAjouter(SpriteBoutton) : 

    # def __init__(self, x, y, largeur, hauteur, chemin_image, contexte, type) :
    #def __init__(self, **kwargs) : 
    def __init__(self, contexte, tabDonnee) :
        # TODO : remove et utiliser les kwargs
        data = cs.ConfigSingleton.getConfig()["boutons_ajout"]
        #print({key:value for (key, value) in data["buton_ajout_gupy"].items()})
        # exec(type_bouton + '(' + self + ', x=' data["x"]...  ')')
        x = data[tabDonnee]["x"]
        y = data[tabDonnee]["y"]
        largeur = data[tabDonnee]["largeur"]
        hauteur = data[tabDonnee]["hauteur"]
        chemin_image = data[tabDonnee]["chemin_image"]
        # super.constructeur()
        SpriteBoutton.__init__(self, x, y, largeur, hauteur, chemin_image)
        
        # element de cet objet hérité
        self.type_poisson = data[tabDonnee]["type_poisson"]
        self.contexte = contexte
        
    def clique(self, contexte) : 
        if contexte.cagnotte > 50 :
            contexte.cagnotte -= 50 
            contexte.ajouteVivant(type_poisson = self.type_poisson)
        

