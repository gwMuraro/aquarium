from PIL import Image

### Utilitaire de flipage d'image pour les png de
#  base qu'on va utiliser pour le début du développement 
### 

img = Image.open("../images/meduse.png")
img.save("../images/meduse_vers_la_droite.png")

img2 = img.transpose(Image.FLIP_LEFT_RIGHT)
img2.save("../images/meduse_vers_la_gauche.png")
