largeur_ref = 1000
hauteur_ref = 600

def calcul_ihm(valeur_en_pourcent, valeur_reference) : 
    return int((int(valeur_en_pourcent.split("%")[0]) * valeur_reference) / 100)
