kasky= input("Annetaanko lisää kolikoita")

while kasky != "ei":
    if kasky == "ryosto":
        print("kolikot ryostetty")
        break
    print("annetaan kolikot")
    kasky = input("annetaanko lisää kolikoita")
else:
    print("hyvästi")

print("ohjelma loppuu")
