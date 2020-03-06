# Classe de coeficient des directions. 
# Ils donnent les multiplicateurs à appliquer à l'axe x et y.
# Le tuple est un triplet qui renvoi le coef_x, coef_y 
# et l'indice dans le tableau des direction de la valeur choisie.

class CoefDirection() : 
    # définition des fonctions utiles 
    def NORD () :       return (0, -1, 0)
    def NORD_EST() :    return (1, -1, 1)
    def EST () :        return (1,  0, 2)
    def SUD_EST () :    return (1,  1, 3)
    def SUD () :        return (0,  1, 4)
    def SUD_OUEST () :  return (-1, 1, 5)
    def OUEST () :      return (-1, 0, 6)
    def NORD_OUEST () : return (-1, -1, 7)

    sTabDirections = [NORD(), NORD_EST(), EST(), SUD_EST(), SUD(), SUD_OUEST(), OUEST(), NORD_OUEST()]

# # TODO : Aymeric : plus de précision dans les tests de cette classe 
# # test 
# print(CoefDirection.sTabDirections[0])
# print(CoefDirection.sTabDirections[1])
# print(CoefDirection.sTabDirections[2])
# print(CoefDirection.sTabDirections[3])
# print(CoefDirection.sTabDirections[4])
# print(CoefDirection.sTabDirections[5])
# print(CoefDirection.sTabDirections[6])
# print(CoefDirection.sTabDirections[7])
