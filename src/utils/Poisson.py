import utils.Direction as Direction
import random

class Poisson : 
    def __init__(self, inertie_max=50, velocite=3) :
        self.inertie = 0 
        self.inertie_max = inertie_max
        self.velocite = velocite
        self.coef_direction = self.changeDirection()

    def changeDirection(self) :
        self.inertie = 0 
        return Direction.CoefDirection.sTabDirections[random.randint(0,7)]
    
    def calculDeplacement(self, x_actuel, y_actuel, largeur, hauteur) : 
        # update de l'inertie 
        self.inertie += 1        

        # variables de retour et de test 
        avance_x = 0 
        avance_y = 0 
        bChange_direction = False
        print(hauteur)
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

    

# # TODO : Aymeric : tester tous les cas possibles selon le template, avec les tests aux bornes
# # Test 
# poisson = Poisson(inertie_max=50, velocite=3)
# poisson.coef_direction = Direction.CoefDirection.NORD() # controle de la direction du poisson 
# print("Inertie = " + str(poisson.inertie) + " | Velocité = " + str(poisson.velocite) + " | Direction : " + str(poisson.coef_direction))

# # Pour la direction Nord
# print("cas normal " + str(poisson.calculDeplacement(50, 50, 60, 40)))
# poisson.coef_direction = Direction.CoefDirection.NORD() # controle de la direction du poisson 

# print("OOB x < 0 " + str(poisson.calculDeplacement(0, 0, 60, 40)))
# poisson.coef_direction = Direction.CoefDirection.NORD() # controle de la direction du poisson 

# print("OOB x > Max" + str(poisson.calculDeplacement(0, 0, 60, 40)))
# poisson.coef_direction = Direction.CoefDirection.NORD() # controle de la direction du poisson 