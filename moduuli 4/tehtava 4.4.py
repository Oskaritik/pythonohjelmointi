import random
oikea_luku = random.randint(1,10)

while True:
    arvaus = int(input("arvaa luku 1-10 valilta: "))
    if arvaus > oikea_luku:
        print("Liian suuri luku")
    elif arvaus < oikea_luku:
        print("Liian pieni luku")
    else:
        print("Oikein!")
        break