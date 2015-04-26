'''
Lista 3 - Exercício 3
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa
anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de
crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos
necessários para que a população do país A ultrapasse ou iguale a população do país B,
mantidas as taxas de crescimento
Felipe Nogueira de Souza
Twitter: @_outrofelipe
'''

pop_A = 80000
pop_B = 200000
cont = 0

while pop_A <= pop_B:
    pop_A += pop_A * 0.03
    pop_B += pop_B * 0.015
    cont += 1

print ("Após %d anos a população de A será de %.2f habitantes e a população de B será de %.2f habitantes." %(cont, pop_A, pop_B))
