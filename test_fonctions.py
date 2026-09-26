from machines import generer_id_machine
from tickets import generer_id_ticket, rechercher_tickets_par_titre

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

tickets_recherche = [
    {"id": 1, "titre": "Problème de souris"},
    {"id": 2, "titre": "Logiciel de paie bloqué"},
    {"id": 3, "titre": "Souris non reconnue"}
]


assert generer_id_ticket(tickets_vides) == 1

assert generer_id_ticket(tickets_avec_identifiants) == 8


assert generer_id_machine(machines_vides) == 1

assert generer_id_machine(machines_avec_identifiants) == 10



resultats_souris = rechercher_tickets_par_titre(tickets_recherche, "SOURIS")
resultats_absents = rechercher_tickets_par_titre(tickets_recherche, "imprimante")

assert len(resultats_souris) == 2

assert resultats_absents == []

print("Tous les tests sont réussis.")