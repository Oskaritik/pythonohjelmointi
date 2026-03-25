import random

def heita_noppaa(tahkojen_maara):
    return random.randint(1, tahkojen_maara)

maksimi = int(input("Anna nopan maksimisilmaluku: "))
silmaluku = 0

while silmaluku != maksimi:
    silmaluku = heita_noppaa(maksimi)
    print(silmaluku)
