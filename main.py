from stockage import sauvegarder_donnees, charger_donnees
from machines import ajouter_machine, afficher_machines, modifier_machine
from tickets import (
    creer_ticket,
    afficher_tickets,
    modifier_statut_ticket,
    supprimer_ticket,
    afficher_tickets_par_statut,
    afficher_tickets_par_gravite,
    afficher_recherche_tickets
    )


def afficher_menu():

    print("=== GESTIONNAIRE DE TICKETS ===")
    print()
    print("1 - Ajouter une machine")
    print("2 - Afficher les machines")
    print("3 - Créer un ticket")
    print("4 - Afficher les tickets")
    print("5 - Modifier le statut d'un ticket")
    print("6 - Supprimer un ticket")
    print("7 - Afficher les tickets par statut")
    print("8 - Afficher les tickets par gravité")
    print("9 - Rechercher un ticket par titre")
    print("10 - Modifier une machine")
    print("0 - Quitter")
    print()


machines, tickets = charger_donnees()
        

while True:

    afficher_menu()
    choix = input("Entrez une commande : ")

    if choix == "1":
        ajouter_machine(machines)
        sauvegarder_donnees(machines, tickets)
    elif choix == "2":
        afficher_machines(machines)
    elif choix == "3":
        creer_ticket(machines, tickets)
        sauvegarder_donnees(machines, tickets)
    elif choix == "4":
        afficher_tickets(tickets)       
    elif choix == "5":
        modifier_statut_ticket(tickets)
        sauvegarder_donnees(machines, tickets)
    elif choix == "6":
        supprimer_ticket(tickets)
        sauvegarder_donnees(machines, tickets)
    elif choix == "7":
        afficher_tickets_par_statut(tickets)
    elif choix == "8":
        afficher_tickets_par_gravite(tickets)
    elif choix == "9":
        afficher_recherche_tickets(tickets)
    elif choix == "10":
        modifier_machine(machines, tickets)
        sauvegarder_donnees(machines, tickets)
    elif choix == "0":
        sauvegarder_donnees(machines, tickets)
        print("Données sauvegardées. Au revoir.")
        break       
    else:
        print("Commande invalide")

