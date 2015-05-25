'''
Passar para Python
Questão C. Entre 1067 e 3627 (inclusive), quantos números são pares e também
divisíveis por 7?
Autor: Felipe Nogueira de Souza
'''
menor = 1067
maior = 3627
cont = 0
while menor <= maior:
    if menor % 2 == 0:
        if menor % 7 == 0:
            cont += 1
    menor += 1
print(cont)
