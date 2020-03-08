import utils.Direction as Direction
import random
from utils.DecorateurPredation import *

class Poisson(ContenantVivant) : 
    def __init__(self, inertie_max=50, velocite=3) :
       ContenantVivant.__init__(self, inertie_max=50, velocite=3)