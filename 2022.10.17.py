# bekérünk két egész számot és irassuk ki a nagyobb számot
"""
szam_1=int(input("Kérek egy egész számot: "))
szam_2=int(input("Kérek még egy egész számot: "))
if szam_1 > szam_2:
    print("Az elso szam nagyobb")
if szam_2 > szam_1:
    print("A második szám nagyobb")
if szam_1==szam_2:
    print("A két szám megegyezik")
"""
"""
szam_1=int(input("Kérek egy egész számot: "))
szam_2=int(input("Kérek még egy egész számot: "))
if szam_1 > szam_2:
    print("szam_1 nagyobb mint szam_2")
elif szam_2 > szam_1:
    print("szam_2 nagyobb mint szam_1")
elif szam_1==szam_2:    
    print("szam_1 megyegyezik s szam_2-vel")
"""
a=int(input("Kérek egy egész számot:"))
b=int(input("Kérek egy egész számot:"))
c=int(input("Kérek egy egész számot:"))
if a < b and c > b:
    print("A kisebb mint b és c nagyobb mint b")
else:
    print("A feltétel hamis")