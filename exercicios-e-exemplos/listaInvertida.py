lista = []
i = 0
while i < 10:
    n = float(input("Informe o %d numero: " %(i+1)))
    lista.append(n)
    i += 1
while i > 0:
    print(lista[i-1])
    i -= 1
