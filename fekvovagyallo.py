szelesseg = int(input("Adja meg a téglalap szélességét! "))
magassag = int(input("Adja meg a téglalap magassagat! "))
T = szelesseg * magassag
if szelesseg > magassag:
    print("Ez egy fekvő téglalap. Területe:",T)
elif szelesseg < magassag:
    print("Ez egy álló téglalap. Területe:",T)
else:
    print("A téglalap egy négyzet. Területe:",T)
