from stockage import sauvegarder_donnees, charger_donnees

from machines import (
    ajouter_machine,
    afficher_machines,
    modifier_machine,
    supprimer_machine
)

from tickets import (
    creer_ticket,
    afficher_tickets,
    modifier_statut_ticket,
    supprimer_ticket,
    afficher_tickets_par_statut,
    afficher_tickets_par_gravite,
    afficher_recherche_tickets
)


def afficher_menu_principal():

    print("=== GESTIONNAIRE DE TICKETS ===")
    print()
    print("1 - Gestion des machines")
    print("2 - Gestion des tickets")
    print("0 - Quitter")


def afficher_menu_machines():
    print("=== GESTION DES MACHINES ===")
    print()
    print("1 - Ajouter une machine")
    print("2 - Afficher les machines")
    print("3 - Modifier une machine")
    print("4 - Supprimer une machine")
    print("0 - Retour au menu principal")


def afficher_menu_tickets():
    print("=== GESTION DES TICKETS ===")
    print()
    print("1 - Créer un ticket")
    print("2 - Afficher les tickets")
    print("3 - Modifier le statut d'un ticket")
    print("4 - Supprimer un ticket")
    print("5 - Afficher les tickets par statut")
    print("6 - Afficher les tickets par gravité")
    print("7 - Rechercher un ticket par titre")
    print("0 - Retour au menu principal")
        

def menu_machines(machines, tickets):

    while True:

        afficher_menu_machines()
        print()
        choix_machine = input("Entrez une commande : ")
        print()

        if choix_machine == "1":
            ajouter_machine(machines)
            sauvegarder_donnees(machines, tickets)
        elif choix_machine == "2":
            afficher_machines(machines)
        elif choix_machine == "3":
            modifier_machine(machines, tickets)
            sauvegarder_donnees(machines, tickets)
        elif choix_machine == "4":
            supprimer_machine(machines, tickets)
            sauvegarder_donnees(machines, tickets)
        elif choix_machine == "0":
            print("Retour au menu principal.")
            break
        else:
            print("Commande invalide.")

        print()


def menu_tickets(machines, tickets):

    while True:

        afficher_menu_tickets()
        print()
        choix_ticket = input("Entrez une commande : ")
        print()

        if choix_ticket == "1":
            creer_ticket(machines, tickets)
            sauvegarder_donnees(machines, tickets)
        elif choix_ticket == "2":
            afficher_tickets(tickets)
        elif choix_ticket == "3":
            modifier_statut_ticket(tickets)
            sauvegarder_donnees(machines, tickets)
        elif choix_ticket == "4":
            supprimer_ticket(tickets)
            sauvegarder_donnees(machines, tickets)
        elif choix_ticket == "5":
            afficher_tickets_par_statut(tickets)
        elif choix_ticket == "6":
            afficher_tickets_par_gravite(tickets)
        elif choix_ticket == "7":
            afficher_recherche_tickets(tickets)
        elif choix_ticket == "0":
            print("Retour au menu principal.")
            break
        else:
            print("Commande invalide.")

        print()


machines, tickets = charger_donnees()


while True:

    afficher_menu_principal()
    print()
    choix = input("Entrez une commande : ")
    print()

    if choix == "1":
        menu_machines(machines, tickets)
    elif choix == "2":
        menu_tickets(machines, tickets)
    elif choix == "0":
        sauvegarder_donnees(machines, tickets)
        print("Données sauvegardées. Au revoir.")
        break       
    else:
        print("Commande invalide.")

    print()
