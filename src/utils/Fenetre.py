import pygame
from pygame.locals import *
import utils.FileReader.ConfigSingleton as cs
import utils.ControlleurJeu as cj


class Fenetre () :  
    config = cs.ConfigSingleton.getConfig()

    #création de la fénêtre principal
    def creationFenetre(self,tailleFenetre):
        # --- Fenêtre  
        #self.dimensions = self.config["aquarium"]["affichage"]*
        self.fond = self.config["fond_fenetre"]["chemin"]
        self.fenetreAquarium = (self.config["aquarium"]["affichage"]["largeur_aquarium"],self.config["aquarium"]["affichage"]["hauteur_aquarium"])
        self.fenetre = pygame.display.set_mode(tailleFenetre, RESIZABLE)
        pygame.display.set_caption("Aquarium")
        # Ajout d'un fond d'écran 
        fond =pygame.image.load(self.fond).convert()# 1200 x 800
        fond=pygame.transform.scale(fond, self.fenetreAquarium)
        pygame.display.flip()
        return fond

    def blit(self,fond,position):
        #cj.gestionEvenements()
        #image = pygame.transform.scale(fond, (700, 600))
        self.fenetre.blit(fond,position)
        
    def fill (self,pos):
        self.fenetre.fill(pos)
        
    def calculFenetre(self,valeurPourcent, reference): 
        return int((int(valeurPourcent.split("%")[0]) * reference)/100)