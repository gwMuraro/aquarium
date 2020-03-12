
def ajoutePoisson(**kwargs) :
    if kwargs["contexte"] != None \
    and kwargs["type"] != None: 
        if contexte.cagnotte >= 50 : 
            contexte.cagnotte -= 50
            contexte.ajouteVivant(type_poisson=type)

    