bekertszam_lista=[]
while True:
    bekertszam = int(input("Adjon meg egy számot"))
    if -5<= bekertszam <=5:
        bekertszam_lista.append(bekertszam)
    else:
        break
print(bekertszam_lista)
print(sum(bekertszam_lista))

