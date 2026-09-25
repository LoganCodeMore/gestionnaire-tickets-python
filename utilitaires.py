def demander_texte(message):
  
    texte = input(message).strip()

    while len(texte) < 1:
  
        print("Vous devez entrer au moins 1 caractere")
        texte = input(message).strip()

    return texte