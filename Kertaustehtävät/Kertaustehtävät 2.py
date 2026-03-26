luvut = []

while True:
    uusi = int(input("uusi arvo: "))

    if uusi == 0:
        print("Hei hei")
        break

    luvut.append(uusi)
    print(f" Lista nyt: {luvut}")
    print(f"Lista järjestyksessä: {sorted(luvut)}")
