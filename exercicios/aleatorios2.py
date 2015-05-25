import random
lista = []
i = 0
while i <= 15:  
    n = (random.randint(10, 100))
    if n not in lista:
        lista.append(n)
        i += 1        

print(lista)

#poderia fazer while len(lista) < 15 e não precisaria da variavel i
#lista.sort() ordena a lista na ordem crescente
