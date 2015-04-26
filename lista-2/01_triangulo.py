'''
Lista 2 - Exercicio 1.
Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem ser
um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
'''

lado1 = float(input('Informe o valor do primeiro lado: '))
lado2 = float(input('Informe o valor do segundo lado: '))
lado3 = float(input('Informe o valor do terceiro lado: '))
            
if (lado1 + lado2) >= lado3 and (lado2 + lado3) >= lado1 and (lado3 + lado1) >= lado2:
    if lado1 == lado2 and lado2 == lado3:
        print ('E um triangulo equilatero, pois todos os lados sao iguais')
    elif lado1 == lado2 or lado2 == lado3:
        print ('E um triangulo isosceles, pois possui dois lados iguais')
    else:
        print ('E um triangulo escaleno, pois todos os lados sao diferentes')
    
else:
    print ('Nao e um triangulo')
