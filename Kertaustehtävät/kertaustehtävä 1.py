luku = int(input("minkä luvun haluat (1-10)"))

print(f"luvun{luku}kertotaulu:")
for i in range (1,11):
    tulos = luku * i
    print(f"{i}*{luku}={tulos}")
