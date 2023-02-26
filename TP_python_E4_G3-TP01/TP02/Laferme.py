from lib.ferme import *
from lib.menu_utils import *

while True:
    print_menu()
    choix = input("Votre choix ? ")
    if choix == "1":
        choix_animal()
    elif choix == "2":
        maferme.crier()
    elif choix == "3":
        if ferme_vide():
            print("La ferme est vide")
        else:
            nom = input("Nom de l'animal à tuer ? ")
            if nom not in maferme.animaux :
                print("Cet animal n'existe pas")
            else:
                tuer_animal(nom)
    elif choix == "4":
        maferme.Nrb_animaux()
    elif choix == "5":
        break
    else:
        print("Choix invalide")