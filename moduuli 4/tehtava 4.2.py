while True:
    tuumat = float(input("anna tuuma määrä (negatiivinen luku lopettaa):" ))

    if tuumat < 0:
        print( "ohjelma lopetataan" )
        break

    senttimetrit = tuumat * 2.54

    print(f" {tuumat} tuuma = {senttimetrit:.2f} cm")
