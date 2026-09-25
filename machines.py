from utilitaires import demander_texte


def ajouter_machine(machines):

    print("Vous avez choisi d'ajouter une machine au parc informatique")
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

def modifier_machine(machines):

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
                            print("La modification du nom sera ajoutée ultérieurement.")

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



