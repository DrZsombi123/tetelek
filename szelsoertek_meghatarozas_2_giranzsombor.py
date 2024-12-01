taroltszavak = []
bekertszo = None
while True:
    bekertszo = input("Adjon meg egy szot")
    if bekertszo != "":
        taroltszavak.append(bekertszo)
    else:
        break
if taroltszavak:
    legkisebb = taroltszavak[0]
    legnagyobb = taroltszavak[0]

    for szo in taroltszavak:
        if szo < legkisebb:
            legkisebb = szo
        if szo > legnagyobb:
            legnagyobb = szo

    print(taroltszavak)
    print(f"{legkisebb},{legnagyobb}")
else:
    print("A lista üres.")
