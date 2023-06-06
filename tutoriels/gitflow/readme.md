# GitFlow : Un guide pour les débutants

GitFlow est une stratégie de gestion de branches Git puissante qui facilite le développement parallèle, la gestion des versions et les hotfixes.

Lien vers une référence visuelle : [GitFlow Cheatsheet](https://danielkummer.github.io/git-flow-cheatsheet/)

## Prérequis

Assurez-vous que Git est installé sur votre machine. Si ce n'est pas le cas, suivez les instructions sur [Git Downloads](https://gitforwindows.org/).

## Installation de GitFlow

Après l'installation de Git, vous pouvez vérifier que GitFlow est bien installé en exécutant :

```sh
git flow version
```

Le cas échéant, vous pouvez télécharger GitFlow depuis [GitHub](https://github.com/nvie/gitflow/wiki/Windows).

## Initialisation de GitFlow

Dans votre terminal, naviguez jusqu'à votre projet, puis initialisez GitFlow :

```sh
cd votre_chemin_de_project
git flow init
```

Répondez aux questions concernant les conventions de nommage des branches. Appuyez sur Enter pour chaque question pour accepter les valeurs par défaut ou utiliser celles définie par votre PO.

## Développement de fonctionnalités avec GitFlow

Créez une nouvelle fonctionnalité sur une branche séparée:

```sh
git flow feature start feature_branch
```

Terminez le développement de la fonctionnalité:

```sh
git flow feature finish feature_branch
```

## Gestion des versions avec GitFlow

Créez une nouvelle version:

```sh
git flow release start 0.1.0
```

Apportez les modifications finales nécessaires à la version. Ensuite, terminez la version:

```sh
git flow release finish '0.1.0'
```

## Gestion des Hotfixes avec GitFlow

Démarrez un hotfix:

```sh
git flow hotfix start hotfix_branch
```

Terminez le hotfix:

```sh
git flow hotfix finish hotfix_branch
```
