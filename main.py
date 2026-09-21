machines = []


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


    elif choix == "4":
        print("Vous avez choisi d'afficher les tickets")


    elif choix == "5":
        print("Vous avez choisi de modifier le statut d'un ticket")


    elif choix == "0":
        print("Au revoir")
        break
        
    else:
        print("Commande invalide")

