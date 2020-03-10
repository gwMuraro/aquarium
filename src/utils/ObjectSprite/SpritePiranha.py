#
#
#

from utils.ObjectSprite import  *


class SpritePiranha(SpriteBase) :
    
    DIRECTIONS_DROITE = [1, 2, 3]
    DIRECTIONS_GAUCHE = [5, 6, 7]
    CHEMIN_PIRANHA_VERS_GAUCHE = "src/images/piranha_vers_la_gauche.png"
    CHEMIN_PIRANHA_VERS_DROITE = "src/images/piranha_vers_la_droite.png"

    def __init__(self, x, y, largeur, hauteur) :
        SpriteBase.__init__(self, x, y, largeur, hauteur, SpritePiranha.CHEMIN_PIRANHA_VERS_DROITE)
        self.velocite = 5
        self.poisson = Poisson(50, self.velocite)
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
        if self.poisson.coef_direction[2] in SpritePiranha.DIRECTIONS_DROITE : 
            self.image = pygame.image.load(SpritePiranha.CHEMIN_PIRANHA_VERS_DROITE)
        if self.poisson.coef_direction[2] in SpritePiranha.DIRECTIONS_GAUCHE : 
            self.image = pygame.image.load(SpritePiranha.CHEMIN_PIRANHA_VERS_GAUCHE)
        
        # redimensionnement de la nouvelle image 
        self.redimensionner(self.rect.width, self.rect.height)

    def devientPredateur(self) : 
        if type(self.poisson).__name__ != DecorationPredateur.__name__ :
            self.poisson = DecorationPredateur(self.poisson)
            #print("DEBUG : Je devient prédateur") 
