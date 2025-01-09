import random

def masodik():
    print("II/A, B, C:")
    lista = []
    for i in range(5):
        vszam:int=random.randint(10, 20)
        print(vszam, "-", end="")
    lista.append(vszam)
    return lista

def kisebb(lista):
    print()
    db:int=0
    i:int=0
    if lista[i]>lista[i]:
        db+=1
    return db

def konzolba_ir(db):
    print("II/D, E:")
    print("Kisebb számok száma: ")

def fajlba_ir(db):
    print("II/F")
    with open("vegeredmeny.txt", "w")as file:
        file.write(str(db)+"/n")
    print("vegeredmeny.txt tartalma: ")
    with open("vegeredmeny.txt", "r")as file:
        for sor in file:
            print(sor.strip())