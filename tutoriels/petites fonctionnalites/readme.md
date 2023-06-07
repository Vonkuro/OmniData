# Découpage du développement de votre application en petites fonctionnalités 

## Introduction

Dans ce tutoriel, nous explorerons comment décomposer le développement de votre application en petites fonctionnalités. Cette approche, particulièrement efficace lorsqu'elle est combinée avec l'application de la méthode Kanban, peut considérablement améliorer votre flux de travail et la qualité du code que vous produisez.

## Pourquoi décomposer en petites fonctionnalités ?

La décomposition du code en petites fonctionnalités a plusieurs avantages. Cela permet un déploiement en continu plus sûr, facilite le débogage et le test, et accélère le retour d'information, ce qui se traduit par une productivité accrue de l'équipe. L'approche par petites fonctionnalités est essentielle au respect des principes DevOps et Agile de livraison continue et d'itération rapide.

## Comment décomposer en petites fonctionnalités

### Identification des fonctionnalités 

La première étape consiste à identifier les fonctionnalités que vous pouvez développer et déployer de manière indépendante. Pour ce faire, vous pouvez utiliser des techniques de modélisation de domaine, comme le [Domain Driven Design](https://martinfowler.com/tags/domain%20driven%20design.html), pour identifier les agrégats et les limites de contexte dans votre application.

```plaintext
Exemple :
- Gestion des utilisateurs
- Traitement des paiements
- Gestion des commandes
- etc.
```

### Priorisation des fonctionnalités 

Une fois que vous avez identifié les fonctionnalités, vous devez les prioriser en fonction de leur valeur pour l'utilisateur et de leur complexité de développement. Vous pouvez utiliser des techniques comme le [MoSCoW](https://www.agilebusiness.org/page/ProjectToolsTemplatesMosco) pour prioriser les fonctionnalités.

```plaintext
Exemple :
1. Gestion des utilisateurs (Must-have)
2. Gestion des commandes (Should-have)
3. Traitement des paiements (Could-have)
```

### Développement et test de chaque fonctionnalité 

Ensuite, vous développez chaque fonctionnalité de manière indépendante, en vous assurant qu'elle est correctement testée avant de passer à la suivante. Pour ce faire, vous pouvez utiliser des pratiques de développement piloté par les tests ([TDD](https://fr.wikipedia.org/wiki/Test_driven_development)) et de développement piloté par le comportement ([BDD](https://fr.wikipedia.org/wiki/Behavior_Driven_Development)).

```plaintext
Exemple : 
- Pour la gestion des utilisateurs, développez et testez d'abord la création d'utilisateurs, puis passez à la modification des utilisateurs, etc.
```

## Utilisation de Kanban pour gérer le développement de petites fonctionnalités

Enfin, utilisez le tableau Kanban que vous avez configuré sur Trello pour gérer le développement de ces petites fonctionnalités. Chaque carte représente une fonctionnalité, et son déplacement à travers les colonnes représente l'avancement de son développement.

```plaintext
Exemple : 
- Créez une carte pour la fonctionnalité "Gestion des utilisateurs". 
- Déplacez la carte de "À faire" à "En cours" lorsque vous commencez le développement. 
- Déplacez la carte de "En cours" à "À tester" une fois le code écrit.
- Déplacez la carte de "À tester" à "Terminé" une fois la revue terminée.
```

Voilà, vous êtes maintenant prêt. Bonne programmation !
