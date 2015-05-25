'''
Questão D. Daniela é uma pessoa muito supersticiosa. Para ela, um número é sortudo
se ele contém o dígito 2 mas não o dígito 7. Então, na opinião dela, quantos números
sortudos existem entre 18644 e 33087, incluindo os extremos?
Autor: Felipe Nogueira de Souza
'''
menor = 18644
maior = 33087
cont = 0
while menor <= maior:
    num = str(menor)
    if '2' in num:
        if '7' not in num:
            cont += 1
    menor += 1
print(cont)
