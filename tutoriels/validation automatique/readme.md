# Validation automatique des petites fonctionnalités

## Introduction

Dans ce tutoriel, nous allons apprendre comment mettre en place une validation automatique pour les petites fonctionnalités de votre application.

Cette approche, en tandem avec l'application de la méthode Kanban et le découpage en petites fonctionnalités, va optimiser la qualité de votre code et votre flux de travail.

## Qu'est-ce que la validation automatique ?

La validation automatique fait référence à l'utilisation de tests automatisés pour valider la fonctionnalité de votre code. Les tests automatisés peuvent être effectués à différents niveaux, des tests unitaires qui vérifient le fonctionnement de petits morceaux de code, aux tests d'intégration qui vérifient comment ces morceaux de code fonctionnent ensemble, et enfin aux tests d'acceptation qui vérifient si le code répond aux exigences de l'utilisateur.

## Comment mettre en place la validation automatique

### Ecriture de tests

La première étape de la mise en place de la validation automatique consiste à écrire des tests pour chaque petite fonctionnalité de votre application. Vous pouvez utiliser le [TDD](https://fr.wikipedia.org/wiki/Test_driven_development) (Test Driven Development) et le [BDD](https://fr.wikipedia.org/wiki/Behavior_Driven_Development) (Behavior Driven Development) pour ce faire.

```plaintext
Exemple :
- Pour une fonctionnalité "création d'utilisateur", vous pouvez écrire un test qui vérifie si un nouvel utilisateur peut être créé avec succès. Voici un exemple de test en TDD avec Jest (JavaScript) :

describe('User creation', () => {
  it('should create a new user successfully', async () => {
    const user = { name: 'John Doe', email: 'john@example.com' };
    const response = await request(app)
      .post('/users')
      .send(user);
    expect(response.status).toBe(201);
    expect(response.body.name).toBe(user.name);
  });
});
```

### Configuration de l'intégration continue

La prochaine étape est de configurer l'intégration continue (CI) pour votre projet. L'intégration continue est une pratique DevOps qui consiste à fusionner les modifications de code des développeurs dans une branche principale de manière régulière, souvent plusieurs fois par jour. Pour cela, vous pouvez utiliser des outils comme GitHub Actions.

```plaintext
Exemple :
- Avec GitHub Actions, vous pouvez configurer un workflow qui se déclenche à chaque push sur la branche principale, et qui exécute tous vos tests automatiquement. Voici un exemple de configuration :

name: CI

on:
  push:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2

    - name: Use Node.js
      uses: actions/setup-node@v2
      with:
        node-version: '14'

    - name: Install dependencies
      run: npm ci

    - name: Run tests
      run: npm test
```

### Utilisation de la revue de code

La revue de code est une autre pratique essentielle pour garantir la qualité du code. C'est le processus d'examen systématique du code source par d'autres développeurs pour détecter et corriger les erreurs qui ont été négligées dans le développement initial.

```plaintext
Exemple :
- Utilisez les pull requests sur GitHub pour la revue de code. Avant de fusionner une branche de fonctionnalités dans la branche principale, ouvrez une pull request et demandez à vos collègues de passer en revue le code. Assurez-vous que chaque pull request comprend une description claire des modifications et qu'elle est liée à une issue pour une meilleure traçabilité.
```

## Intégration avec Kanban

Enfin, vous pouvez intégrer la validation automatique avec le tableau Kanban que vous avez configuré sur Trello. Par exemple, vous pouvez déplacer une carte de "En cours" à "À tester" lorsque tous les tests passent avec succès pour une petite fonctionnalité.


Exemple :
```yaml
name: Integration Tests

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:

    runs-on: ubuntu-latest

    strategy:
      matrix:
        node-version: [14.x]

    steps:
    - uses: actions/checkout@v2

    - name: Use Node.js ${{ matrix.node-version }}
      uses: actions/setup-node@v2
      with:
        node-version: ${{ matrix.node-version }}

    - run: npm ci
    - run: npm install jest --save-dev
    - run: npm run build --if-present
    - run: npm test

    - name: Run integration tests
      run: npm run test:integration
```

Dans cet exemple :

- Nous définissons un workflow qui s'exécute à chaque push ou pull request sur la branche principale.
- Nous définissons une matrice pour tester notre application avec Node.js version 14.
- Nous configurons notre environnement avec Node.js.
- Nous installons les dépendances de notre application avec `npm ci`.
- Nous installons Jest, notre framework de test.
- Nous compilons notre application avec `npm run build`.
- Nous exécutons nos tests unitaires avec `npm test`.
- Enfin, nous exécutons nos tests d'intégration avec `npm run test:integration`.

Veuillez noter que `npm run test:integration` fait référence à un script que vous devez définir dans votre fichier `package.json`, qui démarre vos tests d'intégration. Cela peut varier en fonction de la façon dont vous avez configuré votre projet et vos tests.

```note
Remarque : avant d'implémenter ce workflow, assurez-vous que tous les scripts et les commandes que vous utilisez sont bien configurés dans votre projet. Les erreurs de configuration dans votre fichier `package.json` ou dans votre environnement peuvent entraîner l'échec de ce workflow.
```

Et voilà ! Vous savez ce que signifie la validation automatique en place pour vos petites fonctionnalités. Bonne programmation !
