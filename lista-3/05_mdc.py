'''
Lista 3 - Exercício 5
Dados dois números inteiros positivos, determinar o máximo divisor comum entre eles usando
o algoritmo de Euclides.
Felipe Nogueira de Souza
Twitter: @_outrofelipe
'''

n1 = int(input("Informe o primeiro número para calcular o MDC: "))
n2 = int(input("Informe o segundo número: "))

if n1 > n2:
    maior = n1
    menor = n2
else:
    menor = n1
    maior = n2

r = maior % menor

while r != 0:    
    maior = menor
    menor = r
    r = maior % menor

print ("O MDC de %d e %d é: %d" %(n1, n2, menor))
