import pygame
from pygame.locals import *
import utils.ControlleurJeu as ControlleurJeu
import utils.FileReader.ConfigSingleton as cs
from PIL import Image
#from resizeimage import resizeimage

class Fenetre () : 
    config = cs.ConfigSingleton.getConfig() 
    
    def creationFenetre(self,tailleFenetre,fond):
        # --- Fenêtre  
        #self.dimensions = self.config["aquarium"]["affichage"]*
        self.config = cs.ConfigSingleton.getConfig() 
        self.fenetre = pygame.display.set_mode(tailleFenetre, RESIZABLE)
        pygame.display.set_caption("Aquarium")
        # Ajout d'un fond d'écran 
        fond =pygame.image.load(fond).convert()# 1200 x 800
        pygame.display.flip()
        return fond

    def blit(self,image,position):
        self.fenetre.blit(image,position)
        
    def fill (self,pos):
        self.fenetre.fill(pos)

    def redimension(self,fond):
        for event in pygame.event.get():
            if event.type == pygame.VIDEORESIZE :    
                 print(pygame.display.get_surface().get_size())
                 tailleFenetre = pygame.display.get_surface().get_size()
                 self.fond = fenetre.creationFenetre(tailleFenetre)
                 pygame.display.flip() 