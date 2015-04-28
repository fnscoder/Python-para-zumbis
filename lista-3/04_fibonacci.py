'''
Lista 3 - Exercício 4
A seqüência de Fibonacci é a seguinte: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Sua regra de
formação é simples: os dois primeiros elementos são 1; a partir de então, cada elemento é a
soma dos dois anteriores. Faça um algoritmo que leia um número inteiro calcule o seu número
de Fibonacci. F 1 = 1, F 2 = 1, F 3 = 2, etc.
Felipe Nogueira de Souza
Twitter: @_outrofelipe
'''
n1, n2 = 1, 1
i = 1
num = int(input("Informe um número para calcular o seu fibonacci: "))

print (n1)
while i <= num - 1:    
    print (n2)
    n1, n2 = n2, n1+n2
    i += 1



    

