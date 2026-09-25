# Gestionnaire de tickets informatiques

Premier projet Python réalisé dans le cadre de ma formation personnelle au développement.

## Objectif

Créer une application en terminal permettant de gérer un parc de machines et les incidents informatiques qui leur sont associés.

Ce projet me permet de mettre en pratique les fondamentaux de Python ainsi que l’utilisation de Git et GitHub.

## Fonctionnalités actuelles

### Gestion des machines

- Ajouter une machine au parc informatique
- Enregistrer son nom, son utilisateur et son service
- Afficher la liste des machines enregistrées
- Refuser les saisies textuelles vides

### Gestion des tickets

- Créer un ticket associé à une machine
- Ajouter un titre et une description
- Définir la gravité de l’incident
- Afficher l’ensemble des tickets
- Modifier le statut d’un ticket
- Supprimer un ticket avec une demande de confirmation
- Rechercher un ticket à partir de son identifiant
- Générer automatiquement un identifiant unique
- Filtrer les tickets par statut
- Filtrer les tickets par gravité
- Rechercher des tickets par mot-clés dans leur titre

### Sauvegarde des données

- Sauvegarder automatiquement les machines et les tickets au format JSON
- Charger les données lors du démarrage du programme
- Conserver les modifications après la fermeture de l’application
- Gérer l’absence ou la corruption du fichier de données

Le fichier `donnees.json` est exclu du dépôt Git afin de ne pas publier les données utilisées localement.

## Statuts disponibles

- Nouveau
- En cours
- Résolu
- Fermé

## Niveaux de gravité

- Basse
- Moyenne
- Haute
- Critique

## Technologies utilisées

- Python 3
- JSON
- Git
- GitHub
- Visual Studio Code

## Structure du projet

Le programme est organisé en plusieurs modules afin de séparer les responsabilités et de faciliter sa maintenance.

```text
gestionnaire-tickets-python/
├── main.py
├── machines.py
├── tickets.py
├── stockage.py
├── utilitaires.py
├── README.md
└── .gitignore
```

- `main.py` : affiche le menu principal et coordonne les différentes fonctionnalités
- `machines.py` : contient les fonctions liées à la gestion des machines
- `tickets.py` : contient les fonctions de création, d’affichage, de modification, de suppression, de filtrage et de recherche des tickets
- `stockage.py` : gère le chargement et la sauvegarde des données au format JSON
- `utilitaires.py` : contient les fonctions communes utilisées par plusieurs modules

## Lancer le programme

Python 3 doit être installé sur l’ordinateur.

Cloner le dépôt :

```bash
git clone https://github.com/LoganCodeMore/gestionnaire-tickets-python.git
```

Ouvrir le dossier du projet :

```bash
cd gestionnaire-tickets-python
```

Lancer l’application :

```bash
python main.py
```

Sous Windows, il est également possible d’utiliser :

```bash
py main.py
```

## Utilisation

Après le lancement, le menu principal permet de choisir une action en saisissant son numéro :

```text
=== GESTIONNAIRE DE TICKETS ===

1 - Ajouter une machine
2 - Afficher les machines
3 - Créer un ticket
4 - Afficher les tickets
5 - Modifier le statut d'un ticket
6 - Supprimer un ticket
7 - Afficher les tickets par statut
8 - Afficher les tickets par gravité
9 - Rechercher un ticket par titre
0 - Quitter
```

## État du projet

Le projet est en cours de développement. De nouvelles fonctionnalités et améliorations seront ajoutées progressivement.