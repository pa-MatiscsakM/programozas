# A python lista

# A listák több elem tárolására szolgálnak egyetlen változóban.

lista = ["alma", "banán", "cseresznye"]
print(lista)

lista = ["alma", "banán", "cseresznye", "alma" , "banán"]
print(lista)
print(lista[0])
print(lista[3])


lista = ["alma", "banán", "cseresznye"]
print(len(lista))
hossza = len(lista)
print(hossza)


lista1 = ["alma", "banán", "cseresznye"] # string
lista2 = [1, 5 , 7, 9, 3] # int
lista3 = [True, False, False] # bool

lista = list(("alma", "banán", "cseresznye")) #vegye figyelembe a dupla kerek zárójeleket
print(lista) #['alma', 'banán', 'cseresznye']


# irassuk ki a lista utolsó elemét:
lista = ["alma", "banán", "cseresznye"]
print(lista[2])



lista = ["alma-0", "banán-1", "cseresznye-2", "narancs-3", "kivi4-", "szőlő-5", "mangó-6"]
print(lista[2:5])


lista = ["alma-0", "banán-1", "cseresznye-2", "narancs-3", "kivi4-", "szőlő-5", "mangó-6"]
print(lista[:4])


lista = ["alma-0", "banán-1", "cseresznye-2", "narancs-3", "kivi4-", "szőlő-5", "mangó-6"]
print(lista[2:])
ujlista=lista[2:]
print(ujlista)

#---------------------------------------------------------------------------------------------------------------

lista_10_D_1_csop=[]
lista_10_D_1_csop=["FB", "GM", "HK", "KG", "MM", "OA", "PJ", "PP", "SP", "SM", "SM", "TB", "TS", "TT"]

csop1=[]
csop2=[]
csop3=[]
csop1=lista_10_D_1_csop[0:5]
csop2=lista_10_D_1_csop[5:10]
csop3=lista_10_D_1_csop[10:]
print(csop1)
print(csop2)
print(csop3)

#----------------------------------------------------------------------------------------------------------------

lista_10_D_1_csop=[]
lista_10_D_1_csop=["FB", "GM", "HK", "KG", "MM", "OA", "PJ", "PP", "SP", "SM", "SM", "TB", "TS", "TT"]
print(lista_10_D_1_csop[-4:-1])











