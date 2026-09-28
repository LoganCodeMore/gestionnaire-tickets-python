from utilitaires import demander_texte
from datetime import datetime



def generer_id_ticket(tickets):

    if not tickets:
        identifiant_suivant = 1

        return identifiant_suivant
    

    else:
        identifiants = [ticket['id'] for ticket in tickets]

        identifiant_max = max(identifiants)

        identifiant_suivant = identifiant_max + 1

        return identifiant_suivant


def trouver_ticket_id(tickets, id_ticket):

    for ticket in tickets:

        if ticket['id'] == id_ticket:

            return ticket

    return None

def rechercher_tickets_par_titre(tickets, mot_recherche):

    tickets_trouves = []

    for ticket in tickets:

        if mot_recherche.lower() in ticket['titre'].lower():

            tickets_trouves.append(ticket)

    return tickets_trouves


def afficher_recherche_tickets(tickets):

    if not tickets:
        print("Aucun ticket enregistré.")

    else:

        mot_recherche = demander_texte("Quel mot recherchez-vous ? ")

        tickets_trouves = rechercher_tickets_par_titre(tickets, mot_recherche)

        if not tickets_trouves:
            print("Votre saisie n'apparaît dans aucun titre de ticket.")

        else:
            print(f'=== LISTE DE TICKETS CONTENANT "{mot_recherche}" ===')
            print()
            for ticket in tickets_trouves:
                print(f"ID : {ticket['id']}")
                print(f"Titre : {ticket['titre']}")
                print(f"Gravité : {ticket['gravite']}")
                print(f"Statut : {ticket['statut']}")
                print(f"Date de création : {ticket.get('date_creation', 'Non renseignée')}")
                print("--------------------------------")
                print()


def filtrer_tickets_par_statut(tickets, statut_recherche):

    tickets_filtres = []

    for ticket in tickets:

        if ticket['statut'] == statut_recherche:

            tickets_filtres.append(ticket)

    return tickets_filtres

def filtrer_tickets_par_gravite(tickets, gravite_recherche):

    tickets_filtres = []

    for ticket in tickets:

        if ticket['gravite'] == gravite_recherche:

            tickets_filtres.append(ticket)

    return tickets_filtres


def afficher_tickets_par_gravite(tickets):

    if not tickets:
        print("Aucun ticket enregistré.")

    else:
        gravites_valides = ["Basse", "Moyenne", "Haute", "Critique"]

        for numero, gravite in enumerate(gravites_valides, start=1):
            print(f"{numero} - {gravite}")

        try :
        
            numero_gravite = int(input("Sélectionnez une gravité : "))

            if 1 <= numero_gravite <= len(gravites_valides):

                gravite_recherche = gravites_valides[numero_gravite - 1]

                tickets_filtres = filtrer_tickets_par_gravite(tickets, gravite_recherche)

                if not tickets_filtres:
                    print("Aucun ticket ne correspond à cette gravité.")

                else:
                    print("=== LISTE DES TICKETS PAR GRAVITÉ ===")
                    print()
                    for ticket in tickets_filtres:
                        print(f"ID : {ticket['id']}")
                        print(f"Titre : {ticket['titre']}")
                        print(f"Gravité : {ticket['gravite']}")
                        print(f"Date de création : {ticket.get('date_creation', 'Non renseignée')}")
                        print("-----------------------------")
                        print()

            else:
                print("Ce numéro ne correspond à aucune gravité.")

        except ValueError:
            print("Un nombre est attendu pour filtrer les tickets par gravité.")


def afficher_tickets_par_statut(tickets):

    if not tickets:
        print("Aucun ticket enregistré.")

    else:
        statuts_valides = ["Nouveau", "En cours", "Résolu", "Fermé"]

        for numero, statut in enumerate(statuts_valides, start=1):
            print(f"{numero} - {statut}")


        try :

            numero_statut = int(input("Sélectionnez un statut : "))

            if 1 <= numero_statut <= len(statuts_valides):

                statut_recherche = statuts_valides[numero_statut - 1]

                tickets_filtres = filtrer_tickets_par_statut(tickets, statut_recherche)
                
                if not tickets_filtres:
                    print("Aucun ticket ne correspond à ce statut.")
        
        
                else:
                    print("=== LISTE DES TICKETS PAR STATUT ===")
                    print()
                    for ticket in tickets_filtres:
                        print(f"ID : {ticket['id']}")
                        print(f"Titre : {ticket['titre']}")
                        print(f"Statut : {ticket['statut']}")
                        print(f"Date de création : {ticket.get('date_creation', 'Non renseignée')}")
                        print("------------------------------")
                        print()

            else:
                print("Ce nombre ne correspond à aucun statut.")

        except ValueError:
            print("Un nombre est attendu pour filtrer les tickets par statut.") 



def creer_ticket(machines, tickets):

    print("=== CRÉATION D'UN TICKET ===")
    print()

    if not machines:
        print("Impossible de créer un ticket : aucune machine enregistrée")

    else:
        for numero, machine in enumerate(machines, start=1):
            print(f"Machine {numero}")
            print(f"Nom : {machine['nom']}")
            print(f"Utilisateur : {machine['utilisateur']}")
            print(f"Service : {machine['service']}")
            print("-----------------------------------")
            print()

        try:
            numero_machine = int(input("Quelle machine voulez-vous choisir pour créer un ticket ? "))
            print()

            if 1 <= numero_machine <= len(machines):

                machine_selectionnee = machines[numero_machine - 1]

                print(f"Machine sélectionnée : {machine_selectionnee['nom']}")


                titre_incident = demander_texte("Titre de l'incident : ")
                description_incident = demander_texte("Description de l'incident : ")

                gravites_valides = ["Basse", "Moyenne", "Haute", "Critique"]

                while True:
                    gravite_incident = input("Gravité de l'incident (Basse, Moyenne, Haute, Critique) : ").strip().capitalize()

                    if gravite_incident in gravites_valides:
                        break

                    print("Gravité invalide. Choisissez Basse, Moyenne, Haute ou Critique.")

                date_creation = datetime.now().strftime("%d/%m/%Y %H:%M")

                ticket = {
                    "id": generer_id_ticket(tickets),
                    "machine": machine_selectionnee['nom'],
                    "titre": titre_incident,
                    "description": description_incident,
                    "gravite": gravite_incident,
                    "statut": "Nouveau",
                    "date_creation": date_creation
                }

                tickets.append(ticket)

                print(f"Le ticket {ticket['id']} a été créé avec succès.")
                

            else:
                print("Ce nombre ne correspond pas à un numéro de machine.")

        except ValueError:
            print("Veuillez entrer un nombre.")


def afficher_tickets(tickets):

    if not tickets:
        print("Aucun ticket enregistré.")

    else:
        print("=== LISTE DES TICKETS ===")
        print()

        for ticket in tickets:
            print(f"Ticket {ticket['id']}")
            print(f"Machine : {ticket['machine']}")
            print(f"Titre : {ticket['titre']}")
            print(f"Description : {ticket['description']}")
            print(f"Gravité : {ticket['gravite']}")
            print(f"Statut : {ticket['statut']}")
            print(f"Date de création : {ticket.get('date_creation', 'Non renseignée')}")
            print("--------------------------------------")
            print()


def supprimer_ticket(tickets):

    if not tickets:
        print("Suppression impossible : aucun ticket enregistré.")

    else:
        print("=== LISTE DES TICKETS ===")
        print()
        for ticket in tickets:
            print(f"ID : {ticket['id']}")
            print(f"Titre : {ticket['titre']}")
            print("-----------------------------")
            print()


        try:
            id_supprimer = int(input("Entrez l'identifiant du ticket à supprimer : "))
            print()

            
            ticket_selectionne = trouver_ticket_id(tickets, id_supprimer)

            if ticket_selectionne is None:
                print("Aucun ticket correspondant pour la suppression.")

            else:
                print("Ticket sélectionné : ")
                print(f"ID : {ticket_selectionne['id']}")
                print(f"Titre : {ticket_selectionne['titre']}")
                print("-----------------------------------------")
                print()

                reponse_suppression = input("Voulez-vous supprimer ce ticket ? ").strip().lower()
                print()

                while reponse_suppression != "oui" and reponse_suppression != "non":
                    print("Saisie invalide, pour confirmer la suppression du ticket tapez oui, pour annuler la suppression tapez non.")
                    reponse_suppression = input("Voulez-vous supprimer ce ticket ? ").strip().lower()
                    print()

                if reponse_suppression == "oui":
                    tickets.remove(ticket_selectionne)    
                    print("Suppression confirmée.")

                else:
                    print("Demande de suppression annulée, le ticket est conservé.")


        except ValueError:
            print("Un nombre est attendu pour sélectionner un ticket.")



def modifier_statut_ticket(tickets):

    print("=== MODIFICATION DU STATUT D'UN TICKET ===")
    print()

    if not tickets:
        print("Modification impossible : aucun ticket enregistré.")

    else:

        for ticket in tickets:
            print(f"id : {ticket['id']}")
            print(f"Titre : {ticket['titre']}")
            print(f"Statut : {ticket['statut']}")
            print("------------------------------")
            print()

        try:

            id_ticket_modifier = int(input("Entrez l'id du ticket à modifier : "))

            
            ticket_selectionne = trouver_ticket_id(tickets, id_ticket_modifier)
            

            if ticket_selectionne is None:
                print("Aucun ticket ne correspond à cet identifiant.")

            else:
                print(f"Ticket sélectionné : {ticket_selectionne['titre']}")
                print()

                statuts_valides = ["Nouveau", "En cours", "Résolu", "Fermé"]

                for numero, statut in enumerate(statuts_valides, start=1):
                    print(f"{numero} - {statut}")

                print()

                try:

                    choix_statut = int(input("Choisissez le nouveau statut : "))

                    if 1 <= choix_statut <= len(statuts_valides):
                        nouveau_statut = statuts_valides[choix_statut - 1]

                        ticket_selectionne["statut"] = nouveau_statut

                        print(f"Le statut du ticket {ticket_selectionne['id']} a été modifié : {ticket_selectionne['statut']}")

                    else:
                        print("Ce numéro ne correspond à aucun statut.")


                except ValueError:
                    print("Un nombre est attendu pour modifier le statut du ticket.")


        except ValueError:
            print("L'id du ticket doit être un nombre.")