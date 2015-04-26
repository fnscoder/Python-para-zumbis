'''
Lista 3 - Exercício 4
A seqüência de Fibonacci é a seguinte: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Sua regra de
formação é simples: os dois primeiros elementos são 1; a partir de então, cada elemento é a
soma dos dois anteriores. Faça um algoritmo que leia um número inteiro calcule o seu número
de Fibonacci. F 1 = 1, F 2 = 1, F 3 = 2, etc.Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa
anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de
crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos
necessários para que a população do país A ultrapasse ou iguale a população do país B,
mantidas as taxas de crescimento
Felipe Nogueira de Souza
Twitter: @_outrofelipe
'''
n1 = 1
n2 = 1

num = int(input("Informe um número para calcular o seu fibonacci: "))

print (n1)
while n2 <= num:    
    print (n2)
    n1, n2 = n2, n1+n2



    

