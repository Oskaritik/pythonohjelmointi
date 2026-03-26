sanat = ["omena", "banaani", "talo", "koodaus", "python", "maa"]
pitemmat_sanat = 0

for sana in sanat:
    if len(sana) > 5:
        pitemmat_sanat += 1

print(f"Listassa oli {pitemmat_sanat} sanaa, joissa on yli 5 kirjainta")
