from utils.ControlleurEntites.Decorateur import *

class DecorationPredateur(Decorateur) :
    def __init__ (self, contenantVivant):
        Decorateur.__init__(self, ContenantVivant)

    def estPredateur (self) : 
        return True