'''
Lista 2 - Exercicio 5.
Faça um Programa que leia três números e mostre o menor deles.
'''
num1 = int(input('Informe o primeiro numero: '))
num2 = int(input('Informe o segundo numero: '))
num3 = int(input('Informe o terceiro numero: '))

if num1 <= num2 and num1 <= num3:
    if num2 <= num3:
        maior = num3
    else:
        maior = num2
    menor = num1
elif num2 <= num3:
    if num1 <= num3:
        maior = num3
    else:
        maior = num1
    menor = num2
else:
    if num1 <= num2:
        maior = num2
    else:
        maior = num1
    menor = num3

print ('Maior: %d' %maior)
print ('Menor: %d' %menor)
