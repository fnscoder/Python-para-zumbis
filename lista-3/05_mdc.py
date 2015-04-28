'''
Lista 3 - Exercício 5
Dados dois números inteiros positivos, determinar o máximo divisor comum entre eles usando
o algoritmo de Euclides.
Felipe Nogueira de Souza
Twitter: @_outrofelipe
'''

n1 = int(input("Informe o primeiro número para calcular o MDC: "))
n2 = int(input("Informe o segundo número: "))

while n1 % n2 != 0:    
    n1, n2 = n2, n1 % n2

print ("MDC: %d" %n2)
