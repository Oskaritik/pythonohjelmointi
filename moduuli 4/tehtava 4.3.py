pienin = None
suurin = None

while True:
    syote = input("Anna luku(kun ei mitaan niin lopettaa):")
    if syote == "":
        break

    luku = float(syote)

    if pienin is None or luku < pienin:
        pienin = luku

    if suurin is None or luku > suurin:
        suurin = luku

    if pienin is not None:
        print(f"pienin luku: {pienin}")
        print(f"suurin luku: {suurin}")

    else:
        print("et syöttänyt yhtään lukua")
