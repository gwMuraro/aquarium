from utils.ControlleurEntites.ContenantVivant import ContenantVivant

class Poisson(ContenantVivant) : 
    def __init__(self, inertie_max=50, velocite=3) :
        ContenantVivant.__init__(self, inertie_max=50, velocite=3)
