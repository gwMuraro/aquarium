#!/usr/bin/env python
#encoding: UTF-8

import yaml
import io 

gupy = {
    'deplacement':['inertie',[0],'inertieMax',[50],'velocite',[3],'direction',['coefDirection']],
    'gestionFaim':['faimMax',[30],'faim',[30],'seuilAppetance',[30/3],'valeurNutritive',[60]],
    'argent' :['argentGenere',[10],'periodeGeneration','curseurGeneration',[0]],
    'predation' :['estProie',[True],'estPredateur',[False]],
}

piranha = {
    'deplacement':['inertie',[0],'inertieMax',[50],'velocite',[3],'direction',['coefDirection']],
    'gestionFaim':['faimMax',[30],'faim',[30],'seuilAppetance',[30/3],'valeurNutritive',[60]],
    'argent' :['argentGenere',[10],'periodeGeneration','curseurGeneration',[0]],
    'predation' :['estProie',[False],'estPredateur',[True]],
}


with io.open('gupy.yaml', 'w', encoding='utf8') as outfile:
    yaml.dump(gupy, outfile, default_flow_style=False, allow_unicode=True)
with io.open('piranha.yaml', 'w', encoding='utf8') as outfile:
    yaml.dump(piranha, outfile, default_flow_style=False, allow_unicode=True)