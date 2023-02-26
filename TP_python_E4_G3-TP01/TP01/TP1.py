from tempfile import NamedTemporaryFile
import shutil
import csv

filename = 'test.csv'
fields = ['Nom', 'Prenom', 'Age', 'Ville']


def Afficher():
    with open(filename) as csvfile:
        DictReader_obj = csv.DictReader(csvfile, fieldnames=fields)
        for item in DictReader_obj:
            print(dict(item))


def Verifier(param):
    with open(filename, 'r', encoding='utf8') as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=fields)
        for row in reader:
            if row['Nom'] == param:
                print(row['Nom']+' '+row['Prenom']+' existe déjà')
                return True


def Ajouter():
    with open(filename, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        Nom = input("Entrez votre Nom : ")
        if Verifier(Nom) == True:
            return False
        else:
            Prenom = input("Entrez votre Prenom : ")
            Age = input("Entrez votre Age : ")
            Ville = input("Entrez votre Ville : ")
            writer.writerow({'Nom': Nom, 'Prenom': Prenom,
                             'Age': Age, 'Ville': Ville})


def Modifier():
    tempfile = NamedTemporaryFile(mode='w', delete=False)
    with open(filename, 'r', encoding='utf8') as csvfile, tempfile:
        reader = csv.DictReader(csvfile, fieldnames=fields)
        writer = csv.DictWriter(tempfile, fieldnames=fields)
        param = input("Veuillez entrez un nom pour modifier: ")
        for row in reader:
            if row['Nom'] == param:
                print('La personne à modifier est ',
                      row['Nom']+' '+row['Prenom'])
                Nom = input("Entrez votre Nom :")
                Prenom = input("Entrez votre Prenom : ")
                Age = input("Entrez votre Age : ")
                Ville = input("Entrez votre Ville : ")
                row['Nom'], row['Prenom'], row['Age'], row['Ville'] = Nom, Prenom, Age, Ville
            row = {'Nom': row['Nom'], 'Prenom': row['Prenom'],
                   'Age': row['Age'], 'Ville': row['Ville']}
            writer.writerow(row)
    shutil.move(tempfile.name, filename)


def Supprimer():
    tempfile = NamedTemporaryFile(mode='w', delete=False)
    with open(filename, 'r', encoding='utf8') as csvfile, tempfile:
        reader = csv.DictReader(csvfile, fieldnames=fields)
        writer = csv.DictWriter(tempfile, fieldnames=fields)
        param = input("Veuillez entrez un nom pour supprimer : ")
        lines = list()
        for row in reader:
            lines.append(row)
            if row['Nom'] == param:
                lines.remove(row)
            elif row['Nom'] != param:
                print("Le Nom n'existe pas")
        writer.writerows(lines)
    shutil.move(tempfile.name, filename)


while True:
    print("1.Afficher")
    print("2.Ajouter")
    print("3.Modifier")
    print("4.Supprimer")
    print("5.Quitter le programme")

    choix = input("Votre choix :")
    if choix == "1":
        Afficher()
    elif choix == "2":
        Ajouter()
    elif choix == "3":
        Modifier()
    elif choix == "4":
        Supprimer()
    elif choix == "5":
        break
