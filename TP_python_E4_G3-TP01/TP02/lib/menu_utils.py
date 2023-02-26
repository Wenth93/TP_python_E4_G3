from lib.ferme import *

maferme = Ferme()

def choix_chat():
    nom = input("Nom: ")
    age = input("Age: ")
    return maferme.ajouter_animal(Chat(nom, age))

def choix_chien():
    nom = input("Nom: ")
    age = input("Age: ")
    return maferme.ajouter_animal(Chien(nom, age))

def choix_bovin():
    nom = input("Nom: ")
    age = input("Age: ")
    return maferme.ajouter_animal(Bovin(nom, age))

def choix_ovin():
    nom = input("Nom: ")
    age = input("Age: ")
    return maferme.ajouter_animal(Ovin(nom, age))

def choix_caprin():
    nom = input("Nom: ")
    age = input("Age: ")
    return maferme.ajouter_animal(Caprin(nom, age))

def choix_porcin():
    nom = input("Nom: ")
    age = input("Age: ")
    return maferme.ajouter_animal(Porcin(nom, age))

def choix_volaille():
    nom = input("Nom: ")
    age = input("Age: ")
    return maferme.ajouter_animal(Volaille(nom, age))

def choix_animal():
    choix = ""
    while choix not in ("1","2","3","4","5","6","7","8","9") :
        print("1. Chat")
        print("2. Chien")
        print("4. Bovin")
        print("5. Ovin")
        print("6. Caprin")
        print("7. Porcin")
        print("8. Volaille")
        print("9. Retour")
        choix = input("Votre choix ? ")
        if choix == "1":
            choix_chat()
            choix_animal()
        elif choix == "2":
            choix_chien()
            choix_animal()
        elif choix == "2":
            choix_chien()
            choix_animal()
        elif choix == "3":
            choix_bovin()
            choix_animal()
        elif choix == "4":
            choix_ovin()
            choix_animal()
        elif choix == "5":
            choix_caprin()
            choix_animal()
        elif choix == "6":
            choix_chien()
            choix_animal()
        elif choix == "7":
            choix_porcin()
            choix_animal()
        elif choix == "8":
            choix_volaille()
            choix_animal()
        elif choix == "9":
            break
        else:
            print("Choix invalide")

def print_menu():
    print("Menu")
    print("1. Ajouter un animal")
    print("2. Cri de tous les animaux")
    print("3. Tuer un animal")
    print("4. Nrb d'animaux dans la ferme")
    print("5. Quitter")


def tuer_animal(nom):
    try:
        maferme.tuer_animal(nom)
    except KeyError:
        print("Cet animal n'existe pas")

def ferme_vide():
    if maferme.animaux == {}:
        return True
    return False