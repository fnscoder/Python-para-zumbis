'''
Lista 2 - Exercicio 7.
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a
ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida
em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem
compradas e o preço total. Obs. : somente são vendidos um número inteiro de latas.
'''

area = int(input('Informe a area a ser pintada: '))

if area%54 == 0:
    latas = area / 54
else:
    latas = (area/54) + 1

valor = 80.0 * latas
print ('Voce precisa de %d lata(s)' %latas)
print ('O valor e R$ %.2f' %valor)
print ('Lata(s): %d \nValor R$ %.2f' %(latas, valor))
