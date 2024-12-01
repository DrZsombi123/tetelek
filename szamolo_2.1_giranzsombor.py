lista = ['alma', 'barack', 'szilva', 'körte', 'banán', "Ananász"]
abetu_szamlalo = []
for szo in lista:
    if szo.startswith("a") or szo.startswith("A"):
        abetu_szamlalo.append(szo)
print(abetu_szamlalo)