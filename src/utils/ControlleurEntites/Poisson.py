from utils.ControlleurEntites.ContenantVivant import ContenantVivant
from utils.FileReader.ConfigSingleton import ConfigSingleton

class Poisson(ContenantVivant) : 
    def __init__(self, type_poisson) :

        ContenantVivant.__init__(self, inertie_max=50, velocite=3)

        config = ConfigSingleton.getConfig()[type_poisson]

        # TODO : au vu de ce qu'a fait Aymeric en sand box, il y a peut etre moyen d'améliorer qqchose ici
        # OVERRIDE CONCRET
        # Gestion du déplacement
        self.inertie = config["deplacement"]["inertie"]
        self.inertie_max = config["deplacement"]["inertie_max"]
        self.velocite = config["deplacement"]["velocite"]
        
        # Gestion de la faim
        self.max_faim = config["gestion_faim"]["faim_max"]
        self.faim = config["gestion_faim"]["faim"] 
        self.seuil_appetance = config["gestion_faim"]["seuil_appetance"] 
        self.valeur_nutritive = config["gestion_faim"]["valeur_nutritive"] 

        # Gestion de l'argent
        self.argent_genere = config["argent"]["argent_genere"]
        self.periode_generation = config["argent"]["periode_generation"]
        self.curseur_generation_argent = config["argent"]["curseur_generation"]

        # Gestion de la prédation 
        if config["predation"]["est_predateur"] == True : 
            self.devientPredateur()

        if config["predation"]["est_proie"] == True : 
            self.devientProie()