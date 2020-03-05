# Projet d'Aquarium
Projet périscolaire pour des étudiants qui s'ennuient en cours ou pendant leurs vacances ;)

Ce projet à pour but de donner une petite expérience de développement collaboratif avec des technologies utilisées par beaucoup de tech-engineers. 

Dans ce document nous allons voir comment mettre en place notre environnement de travail et comment utiliser les outils qui sont à notre disposition. 

> ***Disclaimer** : Certaines technologies choisies ne sont pas exploités à 100 % (Docker et Git par exemple). L'objectif est avant tout de se faire une première main sur cesdites technologies en les manipulants, et ainsi aquérir une expérience suffisante pour la suite du cursus universitaire*

# Installation de l'environnement Docker 

## Installation de docker 
* Pour les utilisateur d'**Ubuntu ou Debian** : 
```bash
sudo apt install docker.io
```

* Pour les utilisateurs d'autres distributions ou OS, consultez le site officiel de docker <a href="https://docs.docker.com/install/">ICI</a>

## Créer notre image Docker

Dans ce dépôt git, vous trouverez un dossier ```docker/``` dans lequel vous aurez un ```Dockerfile```. 
* Copiez-collez le contenu de ce fichier dans un fichier nommé ``Dockerfile`` sur votre machine. 
* Ensuite, dans le même répertoire (celui contenant votre Dockerfile), construisez votre image Docker 

```sudo docker build -t aquarium ./```

> `-t` signifie qu'on donne le nom `aquarium` à notre image. `./` signifie qu'on récupère le Dockerfile dans le répertoire courant. 

* Lancez ensuite votre image dans un conteneur (ne vous étonnez pas de la longueur de la commande, on effectue une redirection du serveur graphique vers le PC hôte) : 

```sh
sudo docker run --rm \
        -e DISPLAY=$DISPLAY \
        -v /tmp/.X11-unix:/tmp/.X11-unix \
        -tid \
        --name aqua \
        aquarium
```
> `--rm` supprime un conteneur existant avec ce nom. `-e` liste les variables d'environnement qui nous sont utile pour la redirection de serveur graphique. `-v` monte le volume de la redirection graphique. `-t` le conteneur à un nom.  `-i` le conteneur est en mode interactif.  `-d` le conteneur tourne en arrière plan et ne se reboot pas instantannément à la déconnexion. 

> Une petite digression par la redirection graphique. Un conteneur ne dispose pas d'une carte graphique ou d'un processeur lui permettant d'afficher des images ou fenêtres. On va donc pour cela utiliser le serveur graphique de notre machine, en redirigeant les applications graphiques du conteneur vers son hôte (votre machine). Le principe est simple, mais pour ceux qui veulent aller plus loin, voici <a href="http://fabiorehm.com/blog/2014/09/11/running-gui-apps-with-docker/"> un lien </a> qui va vous interesser


* Votre conteneur tourne maintenant en arrière plan. Vous pouvez vous y connecter via cette commande :
```bash
sudo docker exec -it aqua bash
```
> `-i` pour interactif, `-t` pour indiquer le nom du conteneur à attaquer

Normalement, à ce stade là vous devriez être entré dans votre conteneur. Pour le vérifier, lancez Visual Studio Code avec la commande ```code```. 

# Configurer votre environnement de travail

## Avant tout, vous faites partie du projet...

Demandez moi en message privé sur github ou par mail de vous accepter dans les développeurs du projet.

## Configurer votre GitHub
Le container ne vous connais pas (du moins il ne connait pas votre Git). Il faut donc le configurer avec :

```bash 
git config --global user.name "VOTRE_LOGIN_GITHUB"
git config --global user.email "VOTRE_EMAIL_GITHUB"
```

... soyez pas débiles, faites gaffe au copé-collé, et changez ce qu'il y a dans les guillemets

## Pour tester si tout va bien côté git 

* Récupérez le dépôt avec : 
```bash
git clone https://github.com/gwMuraro/aquarium
```
* Modifiez la partie "Contributeurs" du README en ajoutant votre nom et vos qualifications dans ce projet. 
* Essayez de sauvegarder les changements du readme avec commit et push :
```bash
git commit -am "ajout de VOTRE_NOM dans les contributeurs"
git push
```
## Sauvegarder vos configurations

Maintenant que vous avez fini de configurer votre container, n'oubliez pas de sauvegarder ces changements. Pour sauvegarder des changements sur votre container, retournez sur un bash de votre machine hôte, et faites un "snapshot" de ce container avec les commandes : 

```bash
#récupération de l'ID de votre container actif 
sudo docker ps 

# sauvegarde du container actif en image. 
sudo docker commit <id_du_container>
```
Faites cela à chaque fin de sessions (je trouverai un moyen de l'automatiser). 

Pour la session suivante vous partirez de l'identifiant de l'image que vous avez sauvegardée : 

```bash
# Visualisation de l'identifiant de l'image de la sauvegarde 
sudo docker images

# Relance d'un nouveau container 
sudo docker run --rm \
        -e DISPLAY=$DISPLAY \
        -v /tmp/.X11-unix:/tmp/.X11-unix \
        -tid \
        <id_de_l_image>

# Connexion au conteneur
sudo docker exec -it <id_du_container> bash

```





## Quelques extensions pour Visual Studio Code 

Maintenant que vous êtes prêts à développer, voici une petite liste des extensions VSC à installer que j'apprécie dans le cadre de ce projet : 
- Python (par Microsoft), ou son équivalent, Python pour VSCode
- Pour le Linter (le surligneur d'erreur), vous pouvez prendre Prospector. Flake8 est assez psychorigide, mais en contrepartie les codes sont plus "propres". 

> Pour changer un Linter, faites ```Ctrl+Maj+P```, puis indiquez "Python: Select linter", et choisissez dans la liste). 

- Pygame Snippets, qui va vous permettre d'aller plus vite avec la *Main lib* qu'on utilise. 

# Documentation 

* Pygame 
    * Documentation officielle : https://www.pygame.org/docs/
    
* GitHub : 
    * Documentation officielle : https://git-scm.com/docs

* Docker : 
    * Documentation officielle : https://docs.docker.com/


# Contributeurs

* Gwendal MURARO - Chef de projet, analyste/concepteur, intégrateur et développeur
* Aymeric Adenot - testeur et déeloppeur 
