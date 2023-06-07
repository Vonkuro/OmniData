# GitHub Action pour les Tests Unitaires Python

Cette GitHub Action est conçue pour exécuter des tests unitaires Python à chaque `push` ou `pull_request` sur la branche `dev`. Voici un aperçu de chaque étape.

## Déclencheurs de l'Action

L'action est déclenchée lors d'un `push` ou d'une `pull_request` sur la branche `dev`.

```yml
on:
  push:
    branches:
      - dev
  pull_request:
    branches:
      - dev 
```

## Jobs

Il y a un seul job dans cette action, appelé `build`, qui est exécuté sur une machine virtuelle utilisant la dernière version de Ubuntu.

```yml
jobs:
  build:
    runs-on: ubuntu-latest
```

## Etapes

### Checkout du code source

La première étape est de récupérer le code source du dépôt à l'aide de l'action `actions/checkout@v2`.

```yml
- name: Checkout du code source
  uses: actions/checkout@v2
```

### Vérifier l'installation de Python

Ensuite, nous vérifions la version actuelle de Python sur la machine.

```yml
- name: Vérifier l'installation de Python
  run: python --version
```

### Installer Python

Nous installons ensuite Python à l'aide de l'action `actions/setup-python@v2`, et nous spécifions la version de Python à installer.

```yml
- name: Installer Python
  uses: actions/setup-python@v2
  with:
    python-version: 3.9
```

### Vérifier la nouvelle installation de Python

Nous vérifions ensuite que Python a été correctement installé en affichant sa version.

```yml
- name: Vérifier la nouvelle installation de Python
  run: python --version
```

### Installer les dépendances

Après cela, nous installons les dépendances requises pour exécuter les tests. Ces dépendances sont listées dans un fichier `requirements.txt`.

```yml
- name: Installer les dépendances
  run: pip install -r requirements.txt
```

### Exécuter les tests avec pytest

Enfin, nous exécutons les tests à l'aide de pytest.

```yml
- name: Exécuter les tests avec pytest
  run: python -m pytest
```

Et voilà, nous avons une GitHub Action qui installe Python, installe les dépendances nécessaires et exécute les tests unitaires Python à chaque `push` ou `pull_request` sur la branche `dev`.
