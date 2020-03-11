# Définition d'une classe "foncteur" avec fonction de call back
class Foncteur : 
    def __init__(self, fonction, **kwargs) : 
        # attachement de la fonction de callback à notre instance. 
        setattr(self, "fonctionCallback", fonction(**kwargs))

# définition d'une fonction qui prend une fonction et des parametres optionnels 
def une_fonction_qui_prend_une_fonction_en_parametre (fonction, parametres=None):
    if parametres == None : 
        fonction()
    else : 
        fonction(parametres)

# Kwargs = dictionnaires d'arguments supplémentaires donnés à l'appel de la fonction
# Plus souple : Conseillé
def une_fonction_de_fonction_avec_kwargs(fonction, **kwargs) : 
    fonction(**kwargs)

if __name__ == "__main__":

    # utilsiation de la fonction simple

    def fonction() : 
        print("(fonction sur plusieurs lignes) : coucou")
        print("(fonction sur plusieurs lignes) : coucou2")

    def fonction_parametree(nom): 
        print("(fonction une seule lignes) : coucou" + str(nom))

    def fonction_multi_parametree(params) : 
        print("(fonction avec tableau de params) : " + str(params[0]) + " | " + str(params[1]))

    def fonction_kwargs(**kwargs) : 
        print("fonction Kwargs : ")
        for clef, valeur in kwargs.items() : 
            print("\t" + str(clef) + " : " + str(valeur))

    # test de la fonction simple 
    une_fonction_qui_prend_une_fonction_en_parametre(fonction)
    une_fonction_qui_prend_une_fonction_en_parametre(lambda : print("(fonction lambda) : coucou3"))
    une_fonction_qui_prend_une_fonction_en_parametre(fonction_parametree, parametres = "bruh")
    une_fonction_qui_prend_une_fonction_en_parametre(fonction_multi_parametree, ["Coucou", "ooouuu ?"])
    
    # test de la fonction kwarg 
    une_fonction_de_fonction_avec_kwargs(fonction_kwargs, cc="coucou", dl="david_lafarge", pk="pokemon")
    une_fonction_de_fonction_avec_kwargs(fonction_kwargs)

    # test de la fonction de callback dans une classe
    cl = Foncteur(fonction_kwargs, un="1", deux="deux")
    cl.fonctionCallback

