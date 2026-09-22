machines = []
tickets = []


while True:

    print("=== GESTIONNAIRE DE TICKETS ===")
    print()
    print("1 - Ajouter une machine")
    print("2 - Afficher les machines")
    print("3 - Créer un ticket")
    print("4 - Afficher les tickets")
    print("5 - Modifier le statut d'un ticket")
    print("0 - Quitter")
    print()


    choix = input("Entrez une commande : ")

    if choix == "1":
        print("Vous avez choisi d'ajouter une machine au parc informatique")
        print()

        machine_nom = input("Quel est le nom de la machine ? ")
        machine_utilisateur = input("Quel est l'utilisateur de cette machine ? ")
        machine_service = input("A quel service appartient cette machine ? ")

        machine = {
            "nom": machine_nom,
            "utilisateur": machine_utilisateur,
            "service": machine_service
        }

        machines.append(machine)

        print("La machine a été ajouté au parc informatique.")


    elif choix == "2":
        print("Vous avez choisi d'afficher les machines")
        

        if not machines:
            print("Aucune machines enregistrée dans le parc informatique")

        else :

            print("=== MACHINES DU PARC ===")
            print()

            for numero, machine in enumerate(machines, start=1):
                print(f"Machine {numero}")
                print(f"Nom : {machine['nom']}")
                print(f"Utilisateur : {machine['utilisateur']}")
                print(f"Service : {machine['service']}")
                print()


    elif choix == "3":
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


                    titre_incident = input("Titre de l'incident : ")
                    description_incident = input("Description de l'incident : ")

                    gravite_valides = ["Basse", "Moyenne", "Haute", "Critique"]

                    while True:
                        gravite_incident = input("Gravité de l'incident (Basse, Moyenne, Haute, Critique) : ").strip().capitalize()

                        if gravite_incident in gravite_valides:
                            break

                        print("Gravité invalide. Choisissez Basse, Moyenne, Haute ou Critique.")


                    ticket = {
                        "id": len(tickets) + 1,
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


    elif choix == "4":
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


    elif choix == "5":
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

                ticket_selectionne = None

                for ticket in tickets:
                    if ticket['id'] == id_ticket_modifier:
                        ticket_selectionne = ticket
                        break

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

            

    elif choix == "0":
        print("Au revoir")
        break
        
    else:
        print("Commande invalide")

