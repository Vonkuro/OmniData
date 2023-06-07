# Utilisation sécurisée de GitHub 

Ce tutoriel vous guidera à travers quelques principes essentiels pour utiliser GitHub de manière sécurisée. 

Il est conçu pour les développeurs expérimentés qui débutent avec GitHub et Git.

## Prérequis

Vous devez avoir installé Git et créé un compte GitHub pour suivre ce guide.

## Sécurité du compte

La sécurité de votre compte GitHub est primordiale pour une utilisation sûre.

### Créer un mot de passe fort

Créez un mot de passe unique qui inclut une combinaison de chiffres, de lettres majuscules et minuscules, et de caractères spéciaux.

```note
L'utilisation d'un gestionnaire de mots de passe pour générer et stocker vos mots de passe est fortement recommandée.
```

### Activer l'authentification à deux facteurs

L'authentification à deux facteurs ajoute une couche de sécurité supplémentaire à votre compte. Pour l'activer sur GitHub, suivez ce guide dans la [documentation de GitHub](https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa).

### Génération et ajout de clés SSH à GitHub

L'utilisation de clés SSH pour vous authentifier auprès de GitHub est plus sûre et plus pratique que l'utilisation d'un mot de passe. Vous pouvez suivre ce [guide officiel de GitHub](https://docs.github.com/en/authentication/connecting-to-github-with-ssh) pour générer et ajouter des clés SSH à votre compte GitHub.

## Pratiques de travail sécurisées

### Éviter de commit des secrets

Ne commettez jamais d'informations sensibles, comme les clés API, les mots de passe ou les informations d'identification, dans votre dépôt. Si vous avez accidentellement commis un secret, consultez ce guide pour savoir comment le [supprimer de l'historique](https://docs.github.com/en/authentication/removing-sensitive-data-from-a-repository).

### Utilisation de secrets GitHub

Pour utiliser des secrets sans les commettre, vous pouvez utiliser les secrets GitHub. Vous pouvez en savoir plus sur comment les utiliser dans ce [guide officiel](https://docs.github.com/en/actions/reference/encrypted-secrets).

### Utiliser les revues de code

L'examen du code est une étape importante pour maintenir la qualité du code et la sécurité. Chaque pull request doit être examinée par au moins une autre personne.

### Signaler les problèmes de sécurité

Si vous découvrez un problème de sécurité dans votre code, il est crucial de le signaler immédiatement. Suivez les meilleures pratiques de votre équipe ou de votre entreprise pour la divulgation des problèmes de sécurité. Si le problème est dans un projet open-source hébergé sur GitHub, il est généralement préférable de contacter les mainteneurs directement.

#### note
Si vous découvrez une vulnérabilité de sécurité sur GitHub, ne la divulguez pas publiquement. Suivez le [processus de divulgation responsable](https://bounty.github.com/#reporting) pour signaler la vulnérabilité à GitHub.

