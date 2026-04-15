vuodenajat= [
    "talvi", "kevät", "kevät"
    "kesä", "kevät", "kesä"
    "kesä", "kesä", "syksy"
    "syksy", "syksy", "talvi"
]

kk= int(input("Anna kuukauden numero (1-12): "))

if 1 <= kk <= 12:
    print(vuodenajat[kk-1])
else:
    print("virheellinen kuukausi")
