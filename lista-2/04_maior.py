'''
Lista 2 - Exercicio 4.
Faça um Programa que leia três números e mostre o maior deles.
'''
num1 = int(input('Informe o primeiro numero: '))
num2 = int(input('Informe o segundo numero: '))
num3 = int(input('Informe o terceiro numero: '))

if num1 >= num2 and num1 >= num3:
    print ('O maior e o primeiro numero, %d.' %num1)
elif num2 >= num3:
    print ('O maior e o segundo numero, %d.' %num2)
else:
    print ('O maior e o terceiro numero, %d.' %num3)
