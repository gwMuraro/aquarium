import random 
import pygame
import sys

import utils.CoefDirection as cd

# ====== abs
class ContenantVivant() : 

    def __init__ (self, contenant_vivant):

        self.tabDecorations = list()
        
        self.type_poisson = contenant_vivant.type_poisson

        # Gestion du déplacement
        self.inertie = contenant_vivant.inertie
        self.inertie_max = contenant_vivant.inertie_max
        self.velocite = contenant_vivant.velocite
        self.coef_direction = contenant_vivant.changeDirection()
        
        # Gestion de la faim
        self.max_faim = contenant_vivant.max_faim 
        self.faim = contenant_vivant.faim
        self.seuil_appetance = contenant_vivant.seuil_appetance
        self.valeur_nutritive = contenant_vivant.valeur_nutritive

        # Gestion de l'argent
        self.argent_genere = contenant_vivant.argent_genere
        self.periode_generation = contenant_vivant.periode_generation
        self.curseur_generation_argent = contenant_vivant.curseur_generation_argent


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
            
    def getInformations(self) : 
        chaine = "Poisson de type : " + str(self.type_poisson) + "\n"
        chaine += "\t- Faim = " + str(self.faim) + "\n"
        chaine += "\t- Argent = " + str(self.argent_genere) + "\n"
        chaine += "\t- Période = " + str(self.periode_generation) + "\n"
        chaine += "\t- Est Proie = " + str(self.estProie()) + "\n"
        chaine += "\t- Est Prédateur = " + str(self.estPredateur()) + "\n"

        if self.estPredateur() : 
            chaine += "\t- Proies : \n"
            for proie in self.liste_proies : 
                chaine += "\t\t"+ proie +"\n"

        return chaine


# ============================== ABS ==============================
class Decorateur(ContenantVivant) : 
    def __init__ (self, contenant_vivant):
        ContenantVivant.__init__(self, contenant_vivant)
        #self.contenant_vivant = contenant_vivant

# ============================== Decoration ==============================

class DecorationProie(Decorateur) : 
    def __init__(self, contenant_vivant) :
        Decorateur.__init__(self,contenant_vivant)
    
    def estProie(self) : 
        return True

class DecorationPredateur(Decorateur) :
    
    def __init__ (self, contenant_vivant, liste_proies):
        Decorateur.__init__(self, contenant_vivant)
        self.liste_proies = liste_proies

    def estPredateur (self) : 
        return True