# Présentation du projet 

## Un premier projet collaboratif pour les étudiants

Ce projet à un but ludo-éducatif pour les étudiants de l'association des étudiants de sciences de l'université de La Rochelle (AES - ULR). Pour toute personne motivé, une place et une tâche sera trouvée, qu'importe le niveau de compétence. 

Le but de ce projet est de se faire la main sur des technologies employées dans un environnement de développement professionnel, tout en apprenant des astuces de développement et/ou monter en niveau sur ces-dites technologies. 

## Justification des technologies

### Docker

Docker est un outil de conteneurisation qui utilise la technologie des conteneurs unix en les simplifiants. L'idée principale de son utilisation est de répondre à la question "Pourquoi sur mon PC ça ne marche pas, alors que ça marchait sur le tiens ?". 

Pour résumer son fonctionnement, on crée un conteneur via un DockerFile. Ce conteneur va installer en son sein toutes les dépendances nécessaire au fonctionnement de l'application ainsi que l'application en elle même. Ce conteneur pourra ainsi être partagé (via ce fameux DockerFile). 

Pour ce qui est de la justification : le projet à pour but d'être accessible à tous, et l'environnement de travail conseillé nécessite un temps de mise en place relativement long. Or, avec Docker, il n'y a qu'à l'installer et construire le conteneur avec le Dockerfile présent dans le dossier docker. 

L'inconvénient majeur de la "Docker-isation" de cet environnement de travail est que les conteneurs ne sont pas initialement fait pour faire du grapique. On utilise donc le serveur X11, qui, potentiellement, est complexe à configurer. 

En bref, l'utilisation de docker pour ce projet est conseillée, mais n'est pas obligatoire pour commencer à coder. 

### Git

Git est un must pour tout développeur qui respecte les précepts des méthodes modernes de développement. C'est un outil de gestion des sources qui permet de garder un historique des versions, et qui permet aussi de développer en collaboration. 

Son fonctionnement est simple, les sources sont téléchargées par les développeurs, modifiées de leur côtés, puis sauvegardées et envoyés sur un dépôt en ligne (nous utiliserons GitHub). On peut utiliser plusieurs branches de développements afin d'éviter les conflits de modifications. 

Utiliser Git est simple et très utile pour des projets comme celui-ci. C'est un MUST !

*"Tout seul on va plus vite, ensemble on va plus loin"*

### Python 

Python est un langage agréable à utiliser de part les facilités qu'il apporte pour les développeurs qui le connaissent. Il est doté d'un typage dynamique, de la capacité à faire de l'objet, et de nombreuses librairies. 

L'utilisation de ce langage s'intègre au cursus des nouvelles licences de l'Université de La Rochelle. De plus, pour les étudiants ne le connaissant pas, il sera interessant de sortir des sentiers du C et du JAVA pour débloquer une pensée plus algorithmique/conceptuel que technique. Apprendre de nouveaux langages permet d'en apprendre encore d'autres plus facilements. 

### PyGame

Nous avons besoin de gérer une partie graphique assez complexe dans ce projet. TKinter aurait été trop lacunaire pour nous permettre de la gérer. Nous avons donc choisi le framework pygame, qui est basé sur l'excellente SDL. 

Comme dit plus haut, c'est un framework, pas un moteur. Tout va donc être à faire du côté "simulation", et ce sera un bon exercice, non seulement pour les développeurs, mais aussi pour les graphistes. 

#### YAML 

Nous allons avoir besoin de stocker des informations et de la configuration. Trop peu d'informations pour une base de données, mais assez pour être vite illisible en JSON. Heureusement, le YAML existe. Il s'apparente au JSON mais est plus simple à lire et à écrire pour un humain. De plus la librairie pyYaml est très bien faite pour le management de ce genre de fichiers. 

## Environnement de travail

### VSCode 

VSCode est l'interface de programmation que l'on va utiliser. C'est un puissant IDE qui a beaucoup de fonctionnalités utiles et faciles d'accès (Docker, git, etc.). Il est doté d'un builder paramétrable, d'un débogueur puissant, plein de package pour ce qui est du linting (surlignage d'erreurs) et des snippets (racourcis pour le code). C'est actuellement un des meilleurs IDE du marché, et nous allons l'utiliser pour découvrir son efficacité. 

Il est conseillé, mais pas obligatoire.

### Trello 

Trello est un outil de "gestion des post-it". Il permet d'appliquer une méthodologie AGILE-Scrum avec beaucoup d'efficacité. Il permet de gagner du temps sur l'affectation des tâches, du moment que la gestion du projet est bien faite. 

Nous n'utiliserons pas l'intégralité des fonctionnalités de cet outil (deadlines, buttlers, etc.), car ce projet n'a pas de contrainte temporelle ni de complexité. Sa principale utilité est que tous collaborateur du projet puisse avoir un accès rapide aux tâches qui lui sont confiées, et sur lesquelles il peut échanger (soucis dans l'execution du problème, demande de confirmations, etc.). 



## Directives aux développeurs 

Voici un petit manuel qu'il vous faudra respecter si vous voulez être compris des autres collaborateurs. 

- Commentez votre code, mais soyez intelligent. Ne décrivez pas que ce que la ligne fait, ajoutez des informations qui ne sont pas intuitives. 
- Utilisez des commentaires graphiques. Ces commentaires permettent de visualiser précisément où on se trouve dans les fichiers trop grands. 
- Consultez régulièrements trello et les issues du dépôt github, quit à téléchargez les applications sur votre téléphone. 
- Si vous ne comprenez pas quelque chose dans le code ou sa conception, demandez à celui qui l'a écrit, cela évite de devoir refactoriser du code, et ça peut vous faire gagner du temps. 
- Passez par le papier-crayon, c'est un des meilleurs combos avant de se lancer tête baissée dans le code brute. Les compétences demandés pour ce projet ne sont pas que techniques, mais aussi conceptuelles. 
- N'hésitez pas à regarder les différentes documentations (celle du projet, la documentation de pygame, et dans une moindre mesure, stack overflow).
- Faites attention à vos messages de commit, n'écrivez pas n'importe quoi, soyez précis et succints. 
- Soyez verbeux sur vos noms de variables. ça ne fait pas perdre de temps en les écrivants (auto-complétion) et c'est plus simple à relire. 

## Participer au projet 

Pour participer au projet, Ouvrez une issue et précisez votre nom, prénom et adresse email. Vous pouvez aussi me contacter directement en privé si vous me connaissez. 
