from utilitaires import demander_texte


def ajouter_machine(machines):

    print("=== AJOUT D'UNE MACHINE ===")
    print()
    
    machine_nom = demander_texte("Quel est le nom de la machine ? ")
    while nom_machine_existe(machines, machine_nom):
        print("Ce nom est déjà utilisé par une autre machine.")
        machine_nom = demander_texte("Quel est le nom de la machine ? ")
        
    machine_utilisateur = demander_texte("Quel est l'utilisateur de la machine ? ")
    machine_service = demander_texte("A quel service appartient la machine ? ")

    machine = {
        "id": generer_id_machine(machines),
        "nom": machine_nom,
        "utilisateur": machine_utilisateur,
        "service": machine_service
    }

    machines.append(machine)

    print("La machine a été ajoutée au parc informatique.")



def afficher_machines(machines):
               
    if not machines:
        print("Aucune machine enregistrée dans le parc informatique")

    else:

        print("=== MACHINES DU PARC ===")
        print()

        for numero, machine in enumerate(machines, start=1):
            print(f"Machine {numero}")
            print(f"ID : {machine['id']}")
            print(f"Nom : {machine['nom']}")
            print(f"Utilisateur : {machine['utilisateur']}")
            print(f"Service : {machine['service']}")
            print("-------------------------------------")
            print()



def generer_id_machine(machines):

    if not machines:

        identifiant_suivant = 1

        return identifiant_suivant

    else:

        identifiants = [machine['id'] for machine in machines]

        identifiant_max_machines = max(identifiants)

        identifiant_suivant = identifiant_max_machines + 1

        return identifiant_suivant


def nom_machine_existe(machines, nom_machine):

    for machine in machines:

        if nom_machine.lower() == machine['nom'].lower():
            return True

    return False


def trouver_machine_id(machines, id_machine):

    for machine in machines:

        if machine['id'] == id_machine:
            return machine

    return None

def modifier_machine(machines, tickets):

    if not machines:
        print("Modification impossible : aucune machine enregistrée.")

    else:
        afficher_machines(machines)

        try:

            identifiant_modifier_machine = int(input("Entrez l'identifiant de la machine que vous souhaitez modifier : "))

            machine_trouve = trouver_machine_id(machines, identifiant_modifier_machine)

            if machine_trouve is None:
                print("Aucune machine ne correspond à cet identifiant.")

            else:
                print(f"Machine sélectionnée : {machine_trouve['nom']}")
                print()
                print("1 - Modifier le nom")
                print("2 - Modifier l'utilisateur")
                print("3 - Modifier le service")
                print("0 - Annuler")
                print()

                try:
                    choix_modifier = int(input("Quel type de modification voulez-vous faire sur cette machine ? "))

                    if 0 <= choix_modifier <= 3:

                        if choix_modifier == 0:
                            print("Modification annulée.")

                        elif choix_modifier == 1:
                            ancien_nom = machine_trouve['nom']
                            nouveau_nom = demander_texte("Quel est le nouveau nom de la machine ? ")

                            while nouveau_nom.lower() != ancien_nom.lower() and nom_machine_existe(machines, nouveau_nom):
                                print("Ce nom est déjà utilisé par une autre machine.")
                                nouveau_nom = demander_texte("Quel est le nouveau nom de la machine ? ")

                            machine_trouve['nom'] = nouveau_nom

                            for ticket in tickets:

                                if ticket['machine'].lower() == ancien_nom.lower():
                                    ticket['machine'] = nouveau_nom

                            print(f"La machine {ancien_nom} a été renommée en {nouveau_nom} ainsi que les tickets qui lui sont associés.")


                        elif choix_modifier == 2:
                            nouvel_utilisateur = demander_texte("Quel est le nouvel utilisateur de cette machine ? ")
                            machine_trouve['utilisateur'] = nouvel_utilisateur
                            print("L'utilisateur de cette machine a été modifié.")

                        elif choix_modifier== 3:
                            nouveau_service = demander_texte("À quel nouveau service cette machine appartient ? ")
                            machine_trouve['service'] = nouveau_service
                            print("Le service au quel appartient cette machine a été modifié.")


                    else:
                        print("Ce numéro ne correspond pas à une option de modification.")


                except ValueError:
                    print("Un nombre est attendu pour sélectionner une modification.")


        except ValueError:
            print("Un nombre est attendu pour sélectionner une machine.")



def supprimer_machine(machines, tickets):

    if not machines:
        print("Suppression impossible : aucune machine enregistrée.")

    else:
        afficher_machines(machines)

        try:

            id_supprimer_machine = int(input("Entrez l'identifiant de la machine que vous souhaitez supprimer : "))
            print()

            machine_trouve_supprimer = trouver_machine_id(machines, id_supprimer_machine)

            if machine_trouve_supprimer is None:
                print("Cet identifiant ne correspond à aucune machine.")

            else:
                print(f"Machine sélectionnée : {machine_trouve_supprimer['nom']}")
                print()
                tickets_associes = 0

                for ticket in tickets:

                    if machine_trouve_supprimer['nom'].lower() == ticket['machine'].lower():
                        tickets_associes += 1

                if tickets_associes == 0:
                    reponse_suppression_machine = input("Voulez-vous supprimer cette machine du parc informatique ? ").strip().lower()
                    print()
                    
                    while reponse_suppression_machine != "oui" and reponse_suppression_machine != "non":
                        print("Saisie invalide, pour confirmer la suppression de la machine tapez oui, pour annuler la suppression tapez non.")
                        reponse_suppression_machine = input("Voulez-vous supprimer cette machine du parc informatique ? ").strip().lower()

                    if reponse_suppression_machine == "oui":
                        machines.remove(machine_trouve_supprimer)
                        print("La machine a été supprimée du parc informatique.")

                    else:
                        print("Suppression annulée : la machine est conservée dans le parc informatique.")


                elif tickets_associes == 1:
                    print("Suppression impossible : 1 ticket est associé à cette machine.")

                else:
                    print(f"Suppression impossible : {tickets_associes} tickets sont associés à cette machine.")


        except ValueError:
            print("Un nombre est attendu pour sélectionner une machine.")