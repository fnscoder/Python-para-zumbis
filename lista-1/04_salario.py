'''
Lista 1 - Exercício 4
Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.
Felipe Nogueira de Souza
@_outrofelipe
'''

salario = float(input('Informe o salario: '))
aumento = float(input('Informe a porcentagem de aumento: '))

valorAumento = salario * aumento/100

salarioNovo = salario + valorAumento

print ('O aumento foi de R$ %.2f' %valorAumento)
print ('O novo salario e: R$ %.2f' %salarioNovo)

