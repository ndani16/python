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