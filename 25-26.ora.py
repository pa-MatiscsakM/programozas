"""
print("1.verzió")
szam = 0 
for _ in range(100):    # A for bejáró ciklus, nem összetévesztendő a for számláló ciklussal!
    szam = szam + 1
    print(szam,end=" ") # end megváltoztatom az alapértelmezett \n hatását!
print() # A kiíratás a következő sorban történik!


print("2.verzió")
szam = 1
for _ in range(100):
    print(szam,end=" ")
    szam = szam + 1
print()


print("3.verzió")
szam = 0
for _ in range(1,100):
    szam = szam + 1
    print(szam,end=" ")
print()


print("4.verzió")
szam = 0
for _ in range(1,101,1): # A nem használt változó, de a használata lehetséges! print()
    szam = szam + 1 
    print(szam,end=" ")
print()


print("5.verzió")
szam = 0
for _ in range(5,105,1):
    szam = szam + 1
    print(szam,end=" ")
print()


print("6.verzió")
for _ in range(100): # szam = 0,1,2,3.....,98,99
    print(szam + 1,end=" ")
print()
"""






