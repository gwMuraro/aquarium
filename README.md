# Projet d'Aquarium
Projet périscolaire pour des étudiants qui s'ennuient en cours ou pendant leurs vacances ;)

# Comment commencer à utiliser la chose ? 

### Primo, installer docker 

```sudo apt install docker.io```

### Deuxio, récupérer l'image docker et la lancer 

**copier-coller du DockerFile sur un fichier que vous lacerez.**

Dans le même répertoire : 

```sudo docker build -t aquarium ./```

Cela va construire l'image du container sur lequel vous connecter. Lancez le container avec : 

```sh
sudo docker run --rm \
        -e DISPLAY=$DISPLAY \
        -v /tmp/.X11-unix:/tmp/.X11-unix \
        -tid \
        aquarium
```

Puis connectez vous à ce container pour commencer à travailler : 

```sudo docker exec -it aqua bash```

Lancez Visual Studio Code avec la commande ```code``` pour vérifier que les redirection de serveur graphique marchent bien. 

### Configurer votre environnement de travail

# Contributeurs
* Gwendal MURARO - Chef de projet, analyste/concepteur, intégrateur et développeur

