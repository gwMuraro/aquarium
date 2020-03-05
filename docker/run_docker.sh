echo "VOUS ALLEZ ETRE CONNECTE A VOTRE CONTAINER."
echo "APPUYEZ SUR CTRL+D POUR QUITTER."
echo "VOTRE CONTAINER SERA ENSUITE SAUVEGARDÉ DANS UNE IMAGE DOCKER,"
echo "ET LA PRÉCÉDENTE SERA SUPPRIMÉE DANS LA MESURE DU POSSIBLE"
echo "======================================================================"
str=$(sudo docker images)

# Récupère l'id de l'image 
image_id=$(echo $str | cut -d' ' -f9)
echo "récupération de l'image docker de base : " $image_id

# Roule l'image dans un container
container_id=$(sudo docker run -tid --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix $image_id)
echo "Container ID : " $container_id

# Se connecte au conteneur
echo "CONNEXION AU CONTAINER : ============================================="
sudo docker exec -it $container_id bash
echo "FIN DE CONNEXION AU CONTAINER ========================================"

# Sauvegarde le conteneur
new_image_id=$(sudo docker commit $container_id)

# On termine l'exécution du précédent Docker
sudo docker stop $container_id

# Supprime l'ancienne image pour garder de la place
sudo docker rmi $image_id