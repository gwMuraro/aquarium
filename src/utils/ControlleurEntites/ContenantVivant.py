import random 
import pygame
import sys

import utils.CoefDirection as cd

# ====== abs
class ContenantVivant() : 

    def __init__ (self, inertie_max=50, velocite=3):
        self.tabDecorations = list()
        
        self.type_poisson = "abstract"

        # Gestion du déplacement
        self.inertie = 0 
        self.inertie_max = inertie_max
        self.velocite = velocite
        self.coef_direction = self.changeDirection()
        
        # Gestion de la faim
        self.max_faim = 30 
        self.faim = 30
        self.seuil_appetance = int(self.max_faim / 3)
        self.valeur_nutritive = 60

        # Gestion de l'argent
        self.argent_genere = 10
        self.periode_generation = 2 + random.randint(1, 10)
        self.curseur_generation_argent = 0

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
        import utils.ControlleurJeu as cj
        if x_actuel + largeur + (self.velocite * self.coef_direction[0]) > cj.ControlleurJeu.largeur_aquarium : 
            bChange_direction = True
        if x_actuel + (self.velocite * self.coef_direction[0]) < 0 : 
            bChange_direction = True
        if y_actuel + hauteur + (self.velocite * self.coef_direction[1]) > cj.ControlleurJeu.hauteur_aquarium : 
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
        return cd.CoefDirection.sTabDirections[random.randint(0,7)]
    
    def estPredateur(self) : 
        return False

    def estProie(self) : 
        return False

    def aFaim(self): 
        return self.faim <= self.seuil_appetance

    def mange(self, valeur_nutritive) : 
        self.faim += valeur_nutritive 
        if self.faim > self.max_faim :
            self.faim = self.max_faim
    
    def generationArgent(self) : 
        argent = 0 
        if self.curseur_generation_argent == self.periode_generation : 
            argent = self.argent_genere
            self.curseur_generation_argent = 0 
        else :
            self.curseur_generation_argent += 1 
        return argent

    def devientProie(self) :
        if type(self).__name__ != DecorationProie.__name__ :
            return DecorationProie(self)

    def devientPredateur(self, liste_proies) : 
        if type(self).__name__ != DecorationPredateur.__name__ :
            new = DecorationPredateur(self, liste_proies)
            return new
            
            

# ============================== ABS ==============================
class Decorateur(ContenantVivant) : 
    def __init__ (self, contenant_vivant):
        ContenantVivant.__init__(self)
        #self.contenant_vivant = contenant_vivant

# ============================== Decoration ==============================

class DecorationProie(Decorateur) : 
    def __init__(self, contenant_vivant) :
        Decorateur.__init__(self, contenant_vivant)
        self.type_poisson = contenant_vivant.type_poisson
    
    def estProie(self) : 
        return True

class DecorationPredateur(Decorateur) :
    
    def __init__ (self, contenant_vivant, liste_proies):
        Decorateur.__init__(self, contenant_vivant)
        self.liste_proies = liste_proies
        self.type_poisson = contenant_vivant.type_poisson

    def estPredateur (self) : 
        return True