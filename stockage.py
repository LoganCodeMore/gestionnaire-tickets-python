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