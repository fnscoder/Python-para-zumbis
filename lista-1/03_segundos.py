dias = int(raw_input('Informe a quantidade de dias: '))
horas = int(raw_input('Informe a quantidade de horas: ')) + dias * 24
minutos = int(raw_input('Informe a quantidade de minutos: ')) + horas * 60
segundos = int(raw_input('Informe a quantidade de segundos: ')) + minutos * 60

print 'O total de segundos e: ', segundos

