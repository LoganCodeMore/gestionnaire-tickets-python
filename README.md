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
- Générer automatiquement un identifiant unique pour chaque machine
- Empêcher l'ajout de deux machines portant le même nom
- Modifier le nom, l'utilisateur ou le service d'une machine
- Mettre à jour automatiquement les tickets associés lors du renommage d'une machine
- Supprimer une machine après confirmation
- Empêcher la suppression d'une machine possédant encore des tickets

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
- Enregistrer automatiquement la date et l'heure de création d'un ticket

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

Après le lancement, le menu principal permet d'accéder à la gestion des machines ou à celle des tickets.

```text
=== GESTIONNAIRE DE TICKETS ===

1 - Gestion des machines
2 - Gestion des tickets
0 - Quitter
```

### Menu des machines

```text
=== GESTION DES MACHINES ===

1 - Ajouter une machine
2 - Afficher les machines
3 - Modifier une machine
4 - Supprimer une machine
0 - Retour au menu principal
```

### Menu des tickets

```text
=== GESTION DES TICKETS ===

1 - Créer un ticket
2 - Afficher les tickets
3 - Modifier le statut d'un ticket
4 - Supprimer un ticket
5 - Afficher les tickets par statut
6 - Afficher les tickets par gravité
7 - Rechercher un ticket par titre
0 - Retour au menu principal
```
## Tests

Des tests automatisés vérifient le fonctionnement de certaines fonctions essentielles, notamment la génération des identifiants uniques.

Pour lancer les tests :

```powershell
python test_fonctions.py
```

## État du projet

La version `1.0.0` du gestionnaire de tickets est terminée et stable.

Les fonctionnalités prévues pour cette première version sont implémentées, les données sont sauvegardées au format JSON et les principales fonctions sont couvertes par des tests automatisés.

Le projet pourra évoluer ultérieurement avec une base de données, une interface graphique ou web et une gestion plus avancée des utilisateurs.
