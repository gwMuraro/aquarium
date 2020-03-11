import utils.ControlleurEntites.ContenantVivant as cv

# ============================== ABS ==============================
class Decorateur(cv.ContenantVivant) : 
    def __init__ (self, contenant_vivant):
        cv.ContenantVivant.__init__(self)
        self.contenant_vivant = contenant_vivant

# ============================== Decoration ==============================

class DecorationProie(Decorateur) : 
    def __init__(self, contenant_vivant) :
        Decorateur.__init__(self, contenant_vivant)
        print("je suis une victime " + str(self.estProie()))

    def estProie(self) : 
        return True

class DecorationPredateur(Decorateur) :
    def __init__ (self, contenant_vivant):
        Decorateur.__init__(self, contenant_vivant)

    def estPredateur (self) : 
        return True
