'''
Sorteie 20 inteiros entre 1 e 100 numa lista. Armazene os números pares na lista PAR e os
números ímpares na lista IMPAR. Imprima as três listas.
Autor: Felipe Nogueira de Souza
'''
import random
lista = []
par = []
impar = []
for i in range(20):
    lista.append(random.randint(1, 100))
    if lista[i] % 2 == 0:
        par.append(lista[i])
    else:
        impar.append(lista[i])
print('Lista: ', lista)
print('Pares: ', par)
print('Ímpares: ', impar)
