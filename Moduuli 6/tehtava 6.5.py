def karsi_parittomat(lukulista):

    parilliset = []
    for luku in lukulista:
        if luku % 2 == 0:
            parilliset.append(luku)
    return parilliset

alkuperainen_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
karsittu_lista = karsi_parittomat(alkuperainen_lista)

print("Alkuperäinen lista:", alkuperainen_lista)
print("karsittu lista:", karsittu_lista)
