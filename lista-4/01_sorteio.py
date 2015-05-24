'''
Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra o maior e o menor valor, sem usar
as funções max e min.
Autor: Felipe Nogueira de Souza
'''
import random
lista = []
maior = 1
menor = 100
for i in range(10):
    lista.append(random.randint(1, 100))
    if lista[i] > maior:
        maior = lista[i]
    if lista[i] < menor:
        menor = lista[i]
print('Lista: ', lista)
print('Maior: ', maior)
print('Menor: ', menor)
