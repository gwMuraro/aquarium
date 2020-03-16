# Conception du projet aquarium

## Un mot sur les design patterns

Les design pattern, ou patrons de conception en français, sont des bonnes pratiques de développements qui permettent de résoudre des problèmes en proposant des solutions adaptés et pré-construites. 

### Pattern Singleton

Le pattern singleton est le plus simple à utiliser, à concevoire et à comprendre. Il intervient lors de la créaion d'une instance de classe. 

L'idée est de n'avoir, dans tout le programme, qu'une seule instance d'une même classe. Pour cela on utilise des variables statiques et un constructeur privé. Bon, pour ce qui est du constructeur privé en python, voilà (d'où l'intérêt du nommage verbeux des entités). Cependant, python offre tout ce qu'il faut pour l'implémenter. 

### Pattern Décorateur 

Le pattern décorateur résoud le problème de l'héritage dynamique. Le décorateur hérite de la classe abstraite de l'élément à décorer. Il détient aussi un constructeur qui prend un objet de cette classe abstraite. Ainsi, un décorateur prend la place de l'objet qu'il décore, tout en gardant sa trâce. 

Dans notre projet, un poisson va pouvoir DEVENIR prédateur ou proie d'un autre poisson. On a donc une classe abstraite "ContenantVivant" dont hérite une classe concrète "Poisson" et une classe abstraite "Decorateur" qui a deux héritiers "DecorateurProie" et "DecorateurPredateur". Un poisson est créé. On veut lui donner le satus de prédateur, on remplace donc son instance par un décorateur "DecorateurPredateur" qui a pour paramètre de création notre poisson lui même. 

/\**Ajouter un bout de code + diagramme UML\**/

### Pattern Factory

Un pattern factory (ou usine) permet de centraliser la création de plusieurs types d'objets. On peut faire ces constructeurs sous plusieurs formes, mais une pratique courante vise à dynamiser l'appel au constructeur via les paramètres. On peut ainsi exécuter une chaine de caractère via la fonction exec de python. 

### Pattern MVC 

## L'esprit du projet 

Dans l'idée le projet s'articule autour de plusieurs modules que nous allons développer. 

### Le module de gestion des Sprite 
### Le module de controle des Entités
### Le module de configuration
