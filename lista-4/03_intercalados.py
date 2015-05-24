'''
Faça um programa que crie dois vetores com 10 elementos aleatórios entre 1 e 100. Gere um
terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos
intercalados dos dois outros vetores. Imprima os três vetores.
Autor: Felipe Nogueira de Souza
'''
import random
lista = []
lista2 = []
lista3 = []
for i in range(10):
    lista.append(random.randint(1, 100))
    lista2.append(random.randint(1, 100))
    lista3.append(lista[i])
    lista3.append(lista2[i])
print('Lista 1: ', lista)
print('Lista 2: ', lista2)
print('Lista 3: ', lista3)
