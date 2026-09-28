from machines import (
    generer_id_machine,
    trouver_machine_id,
    nom_machine_existe
)

from tickets import (
    generer_id_ticket,
    rechercher_tickets_par_titre,
    filtrer_tickets_par_statut,
    filtrer_tickets_par_gravite,
    trouver_ticket_id
)

# Données utilisées pour les tests

tickets_vides = []

tickets_avec_identifiants = [
    {"id": 1},
    {"id": 3},
    {"id": 7}
]

machines_vides = []

machines_avec_identifiants = [
    {"id": 2},
    {"id": 5},
    {"id": 9}
]

machines_noms = [
    {"id": 1, "nom": "PC-DEV"},
    {"id": 2, "nom": "PC-ACCUEIL"}
]

tickets_recherche = [
    {"id": 1, "titre": "Problème de souris"},
    {"id": 2, "titre": "Logiciel de paie bloqué"},
    {"id": 3, "titre": "Souris non reconnue"}
]

tickets_filtres = [
    {"id": 1, "statut": "Nouveau", "gravite": "Basse"},
    {"id": 2, "statut": "Résolu", "gravite": "Haute"},
    {"id": 3, "statut": "Nouveau", "gravite": "Critique"}
]

# Tests de génération des identifiants

assert generer_id_ticket(tickets_vides) == 1
assert generer_id_ticket(tickets_avec_identifiants) == 8
assert generer_id_machine(machines_vides) == 1
assert generer_id_machine(machines_avec_identifiants) == 10

# Tests de recherche par titre

resultats_souris = rechercher_tickets_par_titre(tickets_recherche, "SOURIS")
resultats_absents = rechercher_tickets_par_titre(tickets_recherche, "imprimante")

assert len(resultats_souris) == 2
assert resultats_absents == []

# Tests de filtrage

tickets_nouveaux = filtrer_tickets_par_statut(tickets_filtres, "Nouveau")
tickets_fermes = filtrer_tickets_par_statut(tickets_filtres, "Fermé")

assert len(tickets_nouveaux) == 2
assert tickets_fermes == []

tickets_gravite_haute = filtrer_tickets_par_gravite(tickets_filtres, "Haute")
tickets_gravite_moyenne = filtrer_tickets_par_gravite(tickets_filtres, "Moyenne")

assert len(tickets_gravite_haute) == 1
assert tickets_gravite_moyenne == []

# Tests de recherche par identifiant

ticket_trouve = trouver_ticket_id(tickets_filtres, 2)
ticket_absent = trouver_ticket_id(tickets_filtres, 99)

assert ticket_trouve['id'] == 2
assert ticket_absent is None

machine_trouvee = trouver_machine_id(machines_avec_identifiants, 5)
machine_absente = trouver_machine_id(machines_avec_identifiants, 99)

assert machine_trouvee['id'] == 5
assert machine_absente is None

# Tests de contrôle des noms de machines

assert nom_machine_existe(machines_noms, "pc-dev") is True
assert nom_machine_existe(machines_noms, "PC-COMPTA") is False

print("Tous les tests sont réussis.")