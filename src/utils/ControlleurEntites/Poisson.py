from utils.ControlleurEntites.ContenantVivant import ContenantVivant
from utils.FileReader.ConfigSingleton import ConfigSingleton

class Poisson(ContenantVivant) : 
    def __init__(self, type_poisson) :

        config = ConfigSingleton.getConfig()[type_poisson]

        # TODO : n'y a t il pas moyen de décharger tout directement dans un objet avec yaml ? 
        # OVERRIDE CONCRET
        # Gestion du déplacement
        self.type_poisson = type_poisson

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

        # Gestion de la direction 
        self.directions_gauche = config["deplacement"]["direction"]["gauche"]
        self.directions_droite = config["deplacement"]["direction"]["droite"]
        
        ContenantVivant.__init__(self, self)