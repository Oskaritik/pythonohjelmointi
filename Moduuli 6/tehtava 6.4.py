def laske_summa (lukulista):

    summa = 0
    for luku in lukulista:
        summa += luku
    return summa

tekstilista = [2, 4, 6, 8, 10]
listan_summa = laske_summa(tekstilista)
print("Listan lukujen summa on:", listan_summa)
