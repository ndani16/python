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
