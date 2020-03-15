import yaml
import pygame

class ImageSingleton : 
    # __var met l'attribut var en mode privé
    __INSTANCE_IMAGE_SINGLETON = None

    def __init__(self) : 
        
        # Condition de création 
        if ImageSingleton.__INSTANCE_IMAGE_SINGLETON == None : 
            self.images = dict()
            ImageSingleton.__INSTANCE_IMAGE_SINGLETON = self
            print("creation de l'instance de ImageSingleton")

        else : 
            print("Erreur")

    def getImage(chemin_image) : 
        
        # Si l'instance existe, on la prend, sinon on la créée
        if ImageSingleton.__INSTANCE_IMAGE_SINGLETON != None : 
            s = ImageSingleton.__INSTANCE_IMAGE_SINGLETON
        else : 
            s = ImageSingleton()

        # si la clef existe, alors on la renvoie. Sinon on l'ajoute
        try : 
            return s.images[chemin_image]
        except KeyError : 
            print("creation de l'image : " + chemin_image)
            s.images[chemin_image] = pygame.image.load(chemin_image)
            return s.images[chemin_image]
            
