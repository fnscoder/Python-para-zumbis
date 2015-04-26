salario = float(raw_input('Informe o salario: '))
aumento = float(raw_input('Informe a porcentagem de aumento: '))

valorAumento = salario * aumento/100

salarioNovo = salario + valorAumento

print 'O aumento foi de R$ %.2f' % valorAumento
print 'O novo salario e: R$ %.2f' % salarioNovo

