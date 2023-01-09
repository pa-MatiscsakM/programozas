nev = input("Adja meg a keresztnevét: ")
evszamok = int(input("Adja meg az életkorát: "))
if evszamok < 1:
    print("A kora alapján" , nev, "csecsemő!")
elif evszamok < 6:
    print("A kora alapján" , nev, "kisgyerek!")
elif evszamok < 12:
    print("A kora alapján" , nev, "gyerek!")
elif evszamok < 16:
    print("A kora alapján" , nev, "serdülő!")
elif evszamok < 25:
    print("A kora alapján" , nev, "ifjú!")
elif evszamok < 65:
    print("A kora alapján" , nev, "felnőtt!")
else:
    print("A kora alapján" , nev, "nyugdíjas!")
