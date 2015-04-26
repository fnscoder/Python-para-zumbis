'''
Lista 2 - Exercicio 6.
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule
e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê o salário bruto, quanto pagou ao INSS,
quanto pagou ao sindicato e o salário líquido. Observe que Salário Bruto - Descontos = Salário Líquido. Calcule os
descontos e o salário líquido, conforme a tabela abaixo:
a. + Salário Bruto : R$
b. - IR (11%) : R$
c. - INSS (8%) : R$
d. - Sindicato ( 5%) : R$
e. = Salário Liquido : R$
'''

valor_hora = float(input('Qual o valor de sua hora de trabalho: R$ '))
horas_trabalhadas = float(input('Quantas horas voce trabalhou este mes? '))

salario_bruto = valor_hora * horas_trabalhadas
irrf = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - inss - sindicato

print ('+ Salario Bruto: R$ %.2f' %salario_bruto)
print ('- IRRF (11%%): R$ %.2f' %irrf)
print ('- INSS (8%%): R$ %.2f' %inss)
print ('- Sindicato (5%%): R$ %.2f' %sindicato)
print ('= Salario Liquido: R$ %.2f' %salario_liquido)
