from PIL import Image

### Utilitaire de flipage d'image pour les png de
#  base qu'on va utiliser pour le début du développement 
### 

img = Image.open("piranha.png")
img.save("piranha_vers_la_gauche.png")

img2 = img.transpose(Image.FLIP_LEFT_RIGHT)
img2.save("piranha_vers_la_droite.png")