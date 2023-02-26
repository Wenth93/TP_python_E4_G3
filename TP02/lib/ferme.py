class Animal:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def cri(self):
        print("Cri de l'animal")

class Chat(Animal):
    def __init__(self, nom, age):
        super().__init__(nom, age)
        print(f"Le chat {self.nom} est ne ")

    def cri(self):
        print("Miaou")
    
    def __del__(self):
        print(f"Le chat {self.nom} est mort")
    

class Chien(Animal):
    def __init__(self, nom, age):
        super().__init__(nom, age)
        print(f"Le chien {self.nom} est ne ")

    def cri(self):
        print("Ouaf")

    def __del__(self):
        print(f"Le chien {self.nom} est mort")

class Bovin(Animal):
    def __init__(self, nom, age):
        super().__init__(nom, age)
        print(f"Le bovin {self.nom} est ne ")

    def cri(self):
        print("Mbeuhhhh")

    def __del__(self):
        print(f"Le bovin {self.nom} est mort")

class Ovin(Animal):
    def __init__(self, nom, age):
        super().__init__(nom, age)
        print(f"L'ovin {self.nom} est ne ")

    def cri(self):
        print("Mbéh, Mbéhhh")

    def __del__(self):
        print(f"L'ovin {self.nom} est mort")

class Caprin(Animal):
    def __init__(self, nom, age):
        super().__init__(nom, age)
        print(f"Le caprin {self.nom} est ne ")

    def cri(self):
        print("béh, béhhh")

    def __del__(self):
        print(f"Le caprin {self.nom} est mort")

class Porcin(Animal):
    def __init__(self, nom, age):
        super().__init__(nom, age)
        print(f"Le porcin {self.nom} est ne ")

    def cri(self):
        print("Groin-groin")

    def __del__(self):
        print(f"Le porcin {self.nom} est mort ")

class Volaille(Animal):
    def __init__(self, nom, age):
        super().__init__(nom, age)
        print(f"La volaille {self.nom} est ne ")

    def cri(self):
        print("Cocorico")

    def __del__(self):
        print(f"La volaille {self.nom} est mort ")

class Ferme:

    def __init__(self) :
        self.animaux = {}

    def ajouter_animal(self, animal):
        self.animaux[animal.nom] = animal
    
    def tuer_animal(self, nom):
        del self.animaux[nom]

    def crier(self):
        for animal in self.animaux.items():
            animal[1].cri()

    def Nrb_animaux(self):
        print(" Il y actuellement "+str(len(self.animaux))+" animaux/animal dans la ferme") 
