import yaml
class ConfigSingleton : 
    # __var met l'attribut var en mode privé
    __NB_INSTANCES = 0 
    __INSTANCE_CONFIG_SINGLETON = None

    def __init__(self, chemin_config="src/utils/FileReader/gupy.yaml"): 
        
        if ConfigSingleton.__NB_INSTANCES > 0 : 
            print("Erreur faible : le singleton est déjà créé")
        
        else : 
            ConfigSingleton.__NB_INSTANCES += 1
            with open(chemin_config) as fichier : 
                self.doc_yaml = yaml.load(fichier, Loader=yaml.FullLoader)

    def getConfig() : 
        # On envoi l'instance déjà créée 
        if ConfigSingleton.__NB_INSTANCES > 0 : 
            return ConfigSingleton.__INSTANCE_CONFIG_SINGLETON.doc_yaml
        
        # On Crée une instance, puis on l'envoie
        elif ConfigSingleton.__NB_INSTANCES == 0 : 
            ConfigSingleton.__INSTANCE_CONFIG_SINGLETON = ConfigSingleton()
            return ConfigSingleton.__INSTANCE_CONFIG_SINGLETON.doc_yaml
            

# # Test du pattern
# config1 = ConfigSingleton.getConfig()
# print("instance 1 : " + str(config1))

# config2 = ConfigSingleton.getConfig()
# print("instance 2 : " + str(config2))
# print(config2)

# config3 = ConfigSingleton()
# try : 
#     print(config3)
# except Exception : 
#     print("Tout est ok, la config 3 est null")

# # Test avec YAML 
# print(config1["argent"])