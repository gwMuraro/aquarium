from utils.ObjetsSprite.SpriteBase import * 
from utils.ControlleurEntites.Poisson import *
from utils.ControlleurEntites.ContenantVivant import *
from utils.FileReader.ConfigSingleton import ConfigSingleton
from utils.FileReader.ImageSingleton import ImageSingleton

class SpriteVivant(SpriteBase) :
    
    def __init__(self, x, y, largeur, hauteur, type_poisson="gupy") :

        config = ConfigSingleton.getConfig()[type_poisson]

        SpriteBase.__init__(self, x, y, config["affichage"]["largeur"], \
            config["affichage"]["hauteur"], \
            config["affichage"]["liste_sprite_poisson"]["vers_la_gauche"])
        
        self.type_poisson = type_poisson 
        self.poisson = Poisson(type_poisson)
        self.directions_gauche = config["deplacement"]["direction"]["gauche"]
        self.directions_droite = config["deplacement"]["direction"]["droite"]
        self.chemin_images = config["affichage"]["liste_sprite_poisson"]
        
        # Gestion de la prédation
        if config["predation"]["est_predateur"] == True : 
            self.poisson = self.poisson.devientPredateur(config["predation"]["proies"])

        if config["predation"]["est_proie"] == True : 
            self.poisson = self.poisson.devientProie()


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

        if self.poisson.coef_direction[2] in self.directions_gauche : 
            self.image = ImageSingleton.getImage(self.chemin_images["vers_la_gauche"])
        if self.poisson.coef_direction[2] in self.directions_droite : 
            self.image = ImageSingleton.getImage(self.chemin_images["vers_la_droite"])

        # redimensionnement de la nouvelle image 
        self.redimensionner(self.rect.width, self.rect.height)

    def clique(self, contexte) : 
        
        contexte.indice_poisson_actuel = contexte.vivants.index(self)
        print("indice = "+ str(contexte.indice_poisson_actuel))
        contexte.informations_poisson = self.poisson.getInformations()

