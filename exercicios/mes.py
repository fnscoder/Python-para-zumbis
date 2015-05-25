'''
data = input("Informe a data de nascimento (dd/mm/aaaa): ")
data = data.split('/')

if data[1] == '01':
    print("Janeiro")
elif data[1] == '02':
    print("Fevereiro")
elif data[1] == '03':
    print("Março")
elif data[1] == '04':
    print("Abril")
elif data[1] == '05':
    print("Maio")
elif data[1] == '06':
    print("Junho")
elif data[1] == '07':
    print("Julho")
elif data[1] == '08':
    print("Agosto")
elif data[1] == '09':
    print("Setembro")
elif data[1] == '10':
    print("Outubro")
elif data[1] == '11':
    print("Novembro")
elif data[1] == '12':
    print("Dezembro")
else:
    print("Mes inválido")
'''
dia, mes, ano = input('Informe a data de nascimento (dd/mm/aaaa): ').split('/')
meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

print('Você nasceu em: %s de %s de %s' %(dia, meses[int(mes)-1], ano))
