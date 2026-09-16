print("hello world")

#kérj be egy számot és írd ki hogy pozitív vagy negatív!
"""
változó típusok
1 string(szöveg)
2 szám
3 logikai

"""
knev = "Dániel"
egesz = 3
tort = 3.14
print(tort)
lany_e = False
print(lany_e)
print(f"a szám értéke: {egesz}")
print(f"a szám értéke: {tort:.3f}")

#str(5) -> "5"
print(type(str(5)))

#int("5") -> 5
print(type(int("5")))

#float("3.14") -> 3.14
print(type(float("3.14")))

#bool(0) -> False
print(type(bool(0)))

#list()
lista = [1, 1, 9, 5, 6]
print(type(lista))

#set()
halmaz = set(lista)
print(halmaz)

#dict()
szotar = {
    "vnev": "Nagy", 
    "knev": "Dániel", 
    "kor": 19
}
print(type(szotar))

#tuple
t = (1, 10)
print(type(t))

####
'''
szam = int(input("Adjon meg egy számot: ") or "13")
if szam < 0:
    print(f"A {szam} az kisebb mint 0.")
elif szam == 0:
    print(f'A szám a 0.')
else:
    print(f"A {szam} nagyobb mint 0.")
'''

#A gép gondoljon egy számra (1-9) között és találjuk ki.
import random 
rng = random.randint(1,9)
db = 0
# while True:
#     tipp = int(input("Kérem a tippet: "))
#     db += 1
#     if rng != tipp:
#         # if rng < tipp:
#         #     print('Kisebbre gondoltam.')
#         # else:
#         #     print('Nagyobrra gondoltam.')
#         print(f' {'Kisebbre' if rng < tipp else 'Nagyobbra'} gondoltam')
#     else:
#         print("A szám helyes")
#         print(f"{db} lépésben találtad ki.")
#         break

tipp = None
while tipp != rng:
    tipp = int(input("Kérem a tippet: "))
    db += 1
    if rng != tipp:
        print(f' {'Kisebbre' if rng < tipp else 'Nagyobbra'} gondoltam')
    
print("A szám helyes")
print(f"{db} lépésben találtad ki.")