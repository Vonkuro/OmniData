# Documentation Technique des Tests: test_app.py

## Introduction

Le fichier `test_app.py` contient une suite de tests unitaires pour tester les différentes parties de l'application. Il s'agit d'un moyen essentiel de vérifier que le code fonctionne comme prévu, de s'assurer qu'il est robuste et fiable, et de détecter les bugs et les problèmes potentiels.

Les tests unitaires sont généralement organisés autour des fonctionnalités individuelles de l'application, avec des tests distincts pour chaque fonctionnalité.

## Structure des Tests

Chaque fonction de test dans `test_app.py` suit un modèle similaire :

1. Les fonctions de test commencent généralement par une demande de connexion pour obtenir un token d'accès valide. Cela est nécessaire car la plupart des routes API de l'application nécessitent une authentification.

2. Ensuite, la fonction de test effectue une ou plusieurs requêtes API à l'application, en utilisant le client de test fourni par le framework de test.

3. La réponse de chaque requête API est vérifiée pour s'assurer qu'elle a le statut HTTP correct et que les données renvoyées sont celles attendues. Ces vérifications sont effectuées à l'aide des instructions d'assertion.

## Tests Inclus

Voici un bref résumé des différents tests inclus dans `test_app.py` :

- `test_create_app()` : vérifie que l'application est créée correctement.

- `test_create_user()` : teste la création d'un nouvel utilisateur.

- `test_login_user()` : teste la connexion d'un utilisateur existant.

- `test_refresh_token()` : teste le rafraîchissement du token d'accès d'un utilisateur.

- `test_create_component()`, `test_getall_components()`, `test_get_component_by_id()`, `test_delete_component_by_id()` : ces fonctions testent les opérations CRUD sur les composants.

- `test_create_unites()`, `test_getall_unites()`, `test_get_unites_by_id()`, `test_get_unites_by_component_id()`, `test_delete_unites_by_id()` : ces fonctions testent les opérations CRUD sur les unités.

- `test_create_measure()`, `test_getall_measure()`, `test_get_measure_by_id()`, `test_get_measure_by_unite_id()`, `test_delete_measure()` : ces fonctions testent les opérations CRUD sur les mesures.

## Exécution des Tests

Pour exécuter les tests, vous devez généralement utiliser un outil de test approprié pour votre langage et votre framework, comme `pytest` pour Python.

Par exemple, vous pouvez exécuter les tests en utilisant la commande suivante dans le terminal :

```bash
pytest test_app.py
```

Cela exécutera tous les tests dans `test_app.py` et affichera un résumé des résultats à la fin.
