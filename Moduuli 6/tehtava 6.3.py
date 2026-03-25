def gallonat_litroiksi(gallonat):

    return gallonat * 3.785

while True:
    maara_gallonat = float(input("Anna bensiinin määrä gallonoina(negativiinen lopettaaa"))

    if maara_gallonat < 0:
        break

litrat = gallonat_litroiksi(maara_gallonat)
print(f"{maara_gallonat}galloona on {litrat:.2f} litraa")

