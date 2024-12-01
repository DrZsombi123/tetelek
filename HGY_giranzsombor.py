date_list = [ '1983-06-15', '1991-12-07', '1987-03-24', '2001-08-19', '2015-04-03', '1980-11-21', '1999-02-28', '2008-09-12', '1995-01-05', '2020-07-09', '1986-10-30', '1993-05-14', '2011-06-26', '1989-12-18', '2005-03-11', '2018-09-01', '1997-07-20', '2012-11-03', '2023-01-22', '1990-04-09' ]
elott_2000_evszamok = 0
for evszam in date_list:
    ev = int(evszam[:4])
    if ev < 2000:
        elott_2000_evszamok += 1
szemptember_honapok = []
for evszam in date_list:
    honap = int(evszam[5:7])
    if honap == 9:
        szemptember_honapok.append(evszam)
legutolso_ev = int(date_list[0][:4])
for evszam in date_list:
    ev = int(evszam[:4])
    if ev > legutolso_ev:
        legutolso_ev = ev
print("Hány dátum volt 2000 előtt:", elott_2000_evszamok)
print("Szeptember hónapra eső dátumok:", szemptember_honapok)
print("A legutolsó év:", legutolso_ev)
