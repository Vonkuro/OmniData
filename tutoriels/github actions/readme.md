# Tutoriel sur les GitHub Actions

GitHub Actions est une fonctionnalité de CI/CD (Continuous Integration / Continuous Deployment) de GitHub qui vous permet de créer des flux de travail personnalisés pour accélérer votre processus de développement de logiciels.

Avec GitHub Actions, vous pouvez automatiser une grande variété de tâches, des tests unitaires jusqu'au déploiement de l'application.

## Prérequis

Pour suivre ce tutoriel, vous aurez besoin d'un compte GitHub et d'un dépôt où vous pouvez expérimenter avec GitHub Actions.

## Création d'un workflow

Un "workflow" est un ensemble d'actions automatisées qui vous permettent de construire, tester et déployer votre projet. Pour créer un workflow, vous devez créer un fichier YAML dans le répertoire `.github/workflows` de votre dépôt.

```sh
mkdir -p .github/workflows
touch .github/workflows/main.yml
```

## Configuration d'un workflow

Une fois que vous avez créé votre fichier YAML, vous pouvez définir le workflow. Par exemple, voici un workflow de base qui s'exécutera chaque fois que du code est poussé sur la branche "master". 

Pour plus de détails sur chaque action, vous pouvez consulter la [documentation officielle des GitHub Actions](https://docs.github.com/en/actions).

```yaml
name: My First Workflow
on:
  push:
    branches:
      - master
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v2
      - name: Set up Node.js
        uses: actions/setup-node@v2
        with:
          node-version: '14'
      - name: Install dependencies
        run: npm install
      - name: Run tests
        run: npm test
```

## Utilisation des secrets GitHub

Les secrets GitHub sont des variables d'environnement sécurisées que vous pouvez utiliser dans votre workflow. Par exemple, vous pourriez vouloir utiliser une clé API pour déployer une application sur un serveur. Pour créer un secret, allez dans les paramètres de votre dépôt, puis cliquez sur "Secrets". Cliquez sur "New repository secret" et entrez le nom et la valeur du secret.

**N'oubliez jamais d'inclure des informations sensibles directement dans votre fichier de workflow. Utilisez toujours des secrets pour stocker ces informations de manière sécurisée.**

Pour utiliser un secret dans votre workflow, utilisez la syntaxe `${{ secrets.NAME }}`, où "NAME" est le nom de votre secret.

```yaml
- name: Deploy to server
  run: curl -H "Authorization: Bearer ${{ secrets.API_KEY }}" https://my-server.com/deploy
```

## Déploiement d'une Application

Dans cette section, nous aborderons comment déployer une application à partir de GitHub Actions vers un serveur. Supposons que vous ayez un script de déploiement qui nécessite une authentification.

Pour déployer une application, vous pouvez ajouter une étape supplémentaire à la fin de votre workflow :

```yaml
- name: Deploy to Server
  run: ./deploy.sh
  env:
    SERVER: ${{ secrets.SERVER }}
    USERNAME: ${{ secrets.USERNAME }}
    PASSWORD: ${{ secrets.PASSWORD }}
```

Dans cet exemple, nous utilisons le script `deploy.sh` pour déployer notre application. Nous utilisons également des secrets GitHub pour stocker en toute sécurité nos informations d'identification. Vous devrez remplacer `SERVER`, `USERNAME`, et `PASSWORD` par les noms de vos secrets GitHub.

Votre script `deploy.sh` doit être adapté à votre application et à votre serveur. Pour obtenir des exemples de scripts de déploiement, vous pouvez consulter [ce guide](https://developer.github.com/actions/managing-workflows/storing-secrets/).

## Configuration d'un Runner

Un "runner" est une machine hébergeant GitHub Actions et exécutant des jobs. Par défaut, GitHub fournit des runners, mais vous pouvez aussi configurer votre propre runner pour des besoins spécifiques.

**Note : l'utilisation de runners auto-hébergés peut avoir des implications en termes de coûts et de sécurité. Vous êtes responsable de la maintenance et de la mise à jour de vos runners auto-hébergés.**

Pour configurer un runner :

1. Allez dans les paramètres de votre dépôt GitHub.
2. Cliquez sur "Actions" dans la barre latérale gauche.
3. Sous "Self-hosted runners", cliquez sur "Add runner".
4. Suivez les instructions pour installer le runner sur la plateforme de votre choix.

Une fois le runner installé et configuré, vous pouvez spécifier que vous souhaitez l'utiliser dans votre fichier de workflow en ajoutant une ligne `runs-on: self-hosted` à votre job.

```yaml
jobs:
  build:
    runs-on: self-hosted
    steps:
      ...
```

Dans cet exemple, nous avons modifié la ligne `runs-on` pour utiliser notre propre runner au lieu de celui fourni par GitHub. Vous pouvez également spécifier des labels supplémentaires si vous avez plusieurs runners.

## Les Mots-Clés de GitHub Actions YAML

Lorsque vous créez un workflow, il est important de comprendre les différents mots-clés disponibles pour structurer votre fichier YAML.

- `name` : Vous permet de donner un nom à votre workflow. C'est optionnel, mais cela peut rendre votre workflow plus facile à comprendre.
- `on` : Vous permet de spécifier l'événement qui déclenche le workflow. Cela peut être un événement simple comme `push` ou `pull_request`, ou un événement plus complexe avec des filtres.
- `jobs` : Vous permet de définir un ou plusieurs jobs que votre workflow exécutera. Chaque job est une série de `steps` qui sont exécutées en séquence.
- `steps` : Vous permet de définir une série d'étapes pour un job. Chaque étape peut être une action (définie par le mot-clé `uses`) ou une commande shell (définie par le mot-clé `run`).
- `runs-on` : Vous permet de spécifier le type de runner que vous souhaitez utiliser pour votre job. GitHub fournit plusieurs types de runners, comme `ubuntu-latest`, `windows-latest`, et `macos-latest`.
- `env` : Vous permet de définir des variables d'environnement pour une étape ou un job.

Pour une liste complète et des détails supplémentaires, consultez la [documentation officielle de GitHub Actions](https://docs.github.com/en/actions/learn-github-actions/workflow-syntax-for-github-actions).
