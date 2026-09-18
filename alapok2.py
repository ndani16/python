#összegzés tétel
szamok = [5, 6, 7]
# Értékszerinti bejárssal
# osszeg = 0
# for szam in szamok:
#     osszeg += szam
# print(osszeg)

#Index szerinti bejárással
# osszeg = 0
# for i in range(len(szamok)):
#     osszeg += szamok[i]

# print(osszeg)

#Összegzés függvénnyel
def osszegzes(lista):
    """Összeadja a lista-ban levő számokat"""
    osszeg = 0
    for szam in lista:
        osszeg += szam
    
    return osszeg

print(osszegzes(szamok))
print(sum(szamok))

#Add meg a számok átlagát
szamok = [5, 5, 7]
print(f"A számok átlaga: {osszegzes(szamok)/len(szamok):.2f}")

from statistics import mean
print(mean(szamok))

#megszámolás tétel
#hány db páros szám van a megadott számok között?
szamok = [5, 6, 7, 8]

db = 0
for szam in szamok:
    if szam % 2 == 0:
        db += 1

print(f"Páros számok darab száma: {db}.")

#gyakorló feladat
#Add meg a páros számok átlagát

szamok = [5, 6, 7, 8, 3, 2, 5, 4, 9]

paros_osszeg = 0
paros_db = 0
for szam in szamok:
    if szam % 2 == 0:
        paros_db += 1
        paros_osszeg += szam

print(f"A páros számok átaga: {paros_osszeg/paros_db:.2f}")

# Eldöntés
# Lehetséges válaszok: Van, nincs, mind ilyen, egy ilyen sincs
# Visszatérési érték az egy logikai érték
# Pl.: Van e páros száma listában?, A listában minden szám páros?, ...
# Be kell e járni a listát? --> nem
#Van e páros szám a listában?

szamok = [5, 7, 9, 6]
i = 0
while i < len(szamok)  and not (szamok[i] % 2 == 0):
    i += 1

van = i < len(szamok)
print(f"{"Van" if van else "Nincs"} Páros szám a listában.")

#Minden szám páratlan e?
szamok = [5, 7, 6, 9]

i = 0
while i < len(szamok) and not (szamok[i] % 2 == 0):
    i += 1

van = i < len(szamok)
print(f"{"Minden szám" if not van else "Nem minden szám"} páratlan.")

# Eldöntés v2
# Van e páros szám a listában?

van = False
for szam in szamok:
    if szam % 2 == 0:
        van = True
        break

print(f"{"Van" if van else "Nincs"} Páros szám a listában.")

# Kiválasztás tétele
# Ha biztosan tudjuk hogy van olyan elem akkor adjuk meg a sorszámot.
# Visszatérési érték egy sorszám ami a adott tulajdonságú elem a listában.
# Pl.: Hanyadik ember a legmagasabb a listában?
# Hanyadik elem az első páros szám a listában?

szamok = [5, 7, 6, 9]
i = 0
while not (szamok[i] %2 == 0):
    i += 1

print(f"Az első páros elem indexe a(z) {i}, értéke: {szamok[i]}.")