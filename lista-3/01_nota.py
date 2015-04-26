'''
Lista 3 - Exercício 1
Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor
seja inválido e continue pedindo até que o usuário informe um valor válido.
Felipe Nogueira de Souza
Twitter: @_outrofelipe
'''

nota = float(input("Digite uma nota entre 0 e 10: "))

while nota < 0 or nota > 10:
    nota = float(input("A nota digitada é inválida :(\n Digite uma nota entre 0 e 10: "))
print ("A nota digitada foi %.2f." %nota)
