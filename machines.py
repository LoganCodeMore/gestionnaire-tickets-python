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

    print("Vous avez choisi d'afficher les machines")
    print()
               
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