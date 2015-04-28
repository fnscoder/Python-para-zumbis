'''
Lista 3b - Exercício 3
Verifique se um inteiro positivo n é primo.
Felipe Nogueira de Souza
Twitter: @_outrofelipe
'''

n = int(input('Informe um número inteiro positivo: '))
i = 2
primo = True

while i <= n - 1:
    if n % i == 0:
        primo = False
        break
    i += 1

if primo:
    print('O número %d é primo!' %n)
else:
    print('O número %d NÃO é primo!' %n)
