from utils.ObjetsSprite.SpriteBase import *
from utils.ObjetsSprite.CallBacks import *
import utils.FileReader.ConfigSingleton as cs 
import utils.IHM as IHM

class SpriteBoutton(SpriteBase) : 
    
    def __init__(self, x=0, y=0, largeur=0, hauteur=0, chemin_image="") : 
        SpriteBase.__init__(self, x, y, largeur, hauteur, chemin_image)
        self.redimensionner(largeur, hauteur)
        
    def clique(self) :
        pass

    def clicable(self) : 
        return True

class SpriteBouttonAjouter(SpriteBoutton) : 

    def __init__(self, contexte, tabDonnee) :

        data = cs.ConfigSingleton.getConfig()["boutons_ajout"]

        x = IHM.calcul_ihm(data[tabDonnee]["x"], IHM.largeur_ref)
        y = IHM.calcul_ihm(data[tabDonnee]["y"], IHM.hauteur_ref)
        largeur = IHM.calcul_ihm(data[tabDonnee]["largeur"], IHM.largeur_ref)
        hauteur = IHM.calcul_ihm(data[tabDonnee]["hauteur"], IHM.hauteur_ref)
        chemin_image = data[tabDonnee]["chemin_image"]

        SpriteBoutton.__init__(self, x, y, largeur, hauteur, chemin_image)
        
        # element de cet objet hérité
        self.type_poisson = data[tabDonnee]["type_poisson"]
        self.contexte = contexte
        
    def clique(self, contexte) : 
        if contexte.cagnotte > 50 :
            contexte.cagnotte -= 50 
            contexte.ajouteVivant(type_poisson = self.type_poisson)
        

