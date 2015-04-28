'''
Lista 3b - Exercício 4
Dado um número inteiro positivo, determine a sua decomposição em fatores primos
calculando também a multiplicidade de cada fator.
Felipe Nogueira de Souza
Twitter: @_outrofelipe
'''

n = int(input('Informe um número inteiro positivo: '))
i = 2
q = n
d = []
while q >= i:
    
    while q % i == 0:
        q /= i
        d.append(i)
    i += 1
print('Fatoração de %d é: ' %n + str(d))
