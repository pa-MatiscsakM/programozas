# kérjünk be 2 számot (egész szám) utána irasuk ki a nagyobb számot.
elso_szám=int(input("kérek egy egész számot: "))
második_szám=int(input("kérek még egy egész számot: "))
"""
if elso_szám > második_szám:
    print('az első szám nagyobb',elso_szám)
if második_szám>elso_szám:
    print('a második szám nagyobb',második_szám)
"""
if elso_szám > második_szám:
    print(elso_szám)
elif második_szám > elso_szám:
    print(második_szám)
else: print("Az egyik szam megegyezik a amasikkal")