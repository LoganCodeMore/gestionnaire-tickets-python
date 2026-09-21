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

    elif choix == "2":
        print("Vous avez choisi d'afficher les machines")


    elif choix == "3":
        print("Vous avez choisi de créer un ticket")


    elif choix == "4":
        print("Vous avez choisi d'afficher les tickets")


    elif choix == "5":
        print("Vous avez choisi de modifier le statut d'un ticket")


    elif choix == "0":
        print("Au revoir")
        break

        
    else :
        print("Commande invalide")

