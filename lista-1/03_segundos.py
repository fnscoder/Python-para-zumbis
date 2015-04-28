'''
Lista 1 - Exercício 3
Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.
Felipe Nogueira de Souza
@_outrofelipe
'''

dias = int(input('Informe a quantidade de dias: '))
horas = int(input('Informe a quantidade de horas: ')) + dias * 24
minutos = int(input('Informe a quantidade de minutos: ')) + horas * 60
segundos = int(input('Informe a quantidade de segundos: ')) + minutos * 60

print ('O total de segundos e: ', segundos)

