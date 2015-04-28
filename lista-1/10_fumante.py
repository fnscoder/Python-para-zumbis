'''
Lista 1 - Exercício 10
Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o total de dias.
Felipe Nogueira de Souza
@_outrofelipe
'''

cigarros = int(input("Quantos cigarros voce fuma por dia? "))
anos = int(input("Voce fuma a quantos anos? "))

diasPerdidos = (cigarros * anos * 365) / 144

print ('Voce perdeu %d dias de vida! Pare de fumar!!' %diasPerdidos)





