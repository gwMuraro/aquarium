import random 
from utils.Direction import * 

class ContenantVivant() : 

    def __init__ (self, inertie_max=50, velocite=3):
        self.tabDecorations = list()
        self.inertie = 0 
        self.inertie_max = inertie_max
        self.velocite = velocite
        self.coef_direction = self.changeDirection()

    def calculDeplacement(self, x_actuel, y_actuel, largeur, hauteur) : 
        # update de l'inertie 
        self.inertie += 1        

        # variables de retour et de test 
        avance_x = 0 
        avance_y = 0 
        bChange_direction = False

        # Changement de direction si on atteint une fin d'inertie
        if self.inertie >= self.inertie_max : 
            bChange_direction = True

        # Changement de direction par contact avec la bordure
        if x_actuel + largeur + (self.velocite * self.coef_direction[0]) > 800 : 
            bChange_direction = True
        if x_actuel + (self.velocite * self.coef_direction[0]) < 0 : 
            bChange_direction = True
        if y_actuel + hauteur + (self.velocite * self.coef_direction[1]) > 600 : 
            bChange_direction = True
        if y_actuel + (self.velocite * self.coef_direction[1]) < 0 : 
            bChange_direction = True

        # calcul de l'avancement 
        if bChange_direction == True : 
            self.coef_direction = self.changeDirection()
            avance_x = 0 
            avance_y = 0 
        else : 
            avance_x = self.coef_direction[0] * self.velocite
            avance_y = self.coef_direction[1] * self.velocite
        
        # retour des valeurs 
        return avance_x, avance_y
    
    def changeDirection(self) :
        self.inertie = 0 
        return CoefDirection.sTabDirections[random.randint(0,7)]

class Decorateur(ContenantVivant) : 
    def __init__ (self, contenantViant):
        ContenantVivant.__init__(self)
        self.contenantViant = contenantViant

class DecorationPredateur(Decorateur) :
    def __init__ (self, contenantVivant):
        Decorateur.__init__(self, ContenantVivant)
        print("Je suis un prédateur")

class DecorationProie(Decorateur) : 
    def __init__(self, ContenantVivant) :
        Decorateur.__init__(self, ContenantVivant)
        print("je suis une victime")