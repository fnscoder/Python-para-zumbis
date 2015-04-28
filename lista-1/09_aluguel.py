'''
Lista 1 - Exercício 9
Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.
Felipe Nogueira de Souza
@_outrofelipe
'''

km = float(input("Informe a quantidade de km's percorridos: "))
diarias = int(input("Informe a quantidade de diarias: "))

valor = (km * 0.15) + (diarias * 60.0)

print ('O valor a pagar e: R$ %.2f' %valor)

                  
