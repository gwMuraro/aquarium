from utils.ControlleurEntites.ContenantVivant import *

class Decorateur(ContenantVivant) : 
    def __init__ (self, contenantViant):
        ContenantVivant.__init__(self)
        self.contenantViant = contenantViant
    