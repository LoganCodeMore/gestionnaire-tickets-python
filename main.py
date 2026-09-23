import json

def charger_donnees():

    try:
        with open("donnees.json", "r", encoding="utf-8") as fichier:
            donnees = json.load(fichier)

            machines = donnees.get("machines", [])
            tickets = donnees.get("tickets", [])

            return machines, tickets

    except FileNotFoundError:
        return [], []

    except json.JSONDecodeError:
        print("Le fichier de données est invalide. Démarrage avec des listes vides.")
        return [], []

def sauvegarder_donnees(machines, tickets):

    donnees = {
        "machines": machines,
        "tickets": tickets
    }

    with open("donnees.json", "w", encoding="utf-8") as fichier:
        json.dump(donnees, fichier, ensure_ascii=False, indent=4)


def afficher_menu():

    print("=== GESTIONNAIRE DE TICKETS ===")
    print()
    print("1 - Ajouter une machine")
    print("2 - Afficher les machines")
    print("3 - Créer un ticket")
    print("4 - Afficher les tickets")
    print("5 - Modifier le statut d'un ticket")
    print("6 - Supprimer un ticket")
    print("0 - Quitter")
    print()


def demander_texte(message):
  
    texte = input(message).strip()

    while len(texte) < 1:
  
        print("Vous devez entrer au moins 1 caractere")
        texte = input(message).strip()

    return texte


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


def ajouter_machine(machines):

    print("Vous avez choisi d'ajouter une machine au parc informatique")
    print()
    
    machine_nom = demander_texte("Quel est le nom de la machine ? ")
    machine_utilisateur = demander_texte("Quel est l'utilisateur de la machine ? ")
    machine_service = demander_texte("A quel service appartient la machine ? ")

    machine = {
        "nom": machine_nom,
        "utilisateur": machine_utilisateur,
        "service": machine_service
    }

    machines.append(machine)

    print("La machine a été ajoutée au parc informatique.")


def afficher_machines(machines):

    print("Vous avez choisi d'afficher les machines")
    print()
               
    if not machines:
        print("Aucune machine enregistrée dans le parc informatique")

    else:

        print("=== MACHINES DU PARC ===")
        print()

        for numero, machine in enumerate(machines, start=1):
            print(f"Machine {numero}")
            print(f"Nom : {machine['nom']}")
            print(f"Utilisateur : {machine['utilisateur']}")
            print(f"Service : {machine['service']}")
            print("-------------------------------------")
            print()


def creer_ticket(machines, tickets):

    print("Vous avez choisi de créer un ticket")
    print()

    if not machines:
        print("Impossible de créer un ticket : aucune machine enregistrée")

    else:
        for numero, machine in enumerate(machines, start=1):
            print(f"Machine {numero}")
            print(f"Nom : {machine['nom']}")
            print(f"Utilisateur : {machine['utilisateur']}")
            print(f"Service : {machine['service']}")
            print()

        try:
            numero_machine = int(input("Quelle machine voulez-vous choisir pour créer un ticket ? "))

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


                ticket = {
                    "id": generer_id_ticket(tickets),
                    "machine": machine_selectionnee['nom'],
                    "titre": titre_incident,
                    "description": description_incident,
                    "gravite": gravite_incident,
                    "statut": "Nouveau"
                }

                tickets.append(ticket)

                print(f"Le ticket {ticket['id']} a été créé avec succès.")
                

            else:
                print("Ce nombre ne correspond pas à un numéro de machine.")

        except ValueError:
            print("Veuillez entrer un nombre.")


def afficher_tickets(tickets):

    print("Vous avez choisi d'afficher les tickets")
    print()

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

                while reponse_suppression != "oui" and reponse_suppression != "non":
                    print("Saisie invalide, pour confirmer la suppression du ticket tapez oui, pour annuler la suppression tapez non.")
                    reponse_suppression = input("Voulez-vous supprimer ce ticket ? ").strip().lower()

                if reponse_suppression == "oui":
                    tickets.remove(ticket_selectionne)    
                    print("Suppression confirmée.")

                else:
                    print("Demande de suppression annulée, le ticket est conservé.")


        except ValueError:
            print("Un nombre est attendu pour sélectionner un ticket.")



def modifier_statut_ticket(tickets):

    print("Vous avez choisi de modifier le statut d'un ticket")
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
    elif choix == "0":
        sauvegarder_donnees(machines, tickets)
        print("Données sauvegardées. Au revoir.")
        break       
    else:
        print("Commande invalide")

