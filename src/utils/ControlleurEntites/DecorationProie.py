from utils.ControlleurEntites.Decorateur import *

class DecorationProie(Decorateur) : 
    def __init__(self, ContenantVivant) :
        Decorateur.__init__(self, ContenantVivant)
        print("je suis une victime " + str(self.estProie()))

    def estProie(self) : 
        return True