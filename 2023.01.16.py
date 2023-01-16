t = [6, 5, 3, 1, 8, 7, 2, 4, 11, 9, 14, 10, 12]
lista_hossza=len(t)
print(f"A lista hossza: {lista_hossza}")
for i in range(lista_hossza-1, 0, -1):
    for j in range(0, i):
        if t[j] > t[j+1]:    
            tmp= t[j+1]
            t[j+1]= t[j]
            t[j]= tmp
    print(f"{t} i = {i} j = {j}")
