'''f = open('surf.txt')
for linha in f:
    print(linha.strip())  #o .strip retira o caracter de controle que faz pular linha (/n)
f.close()'''
notas = []
with open('surf.txt') as f:
    for linha in f:
        nome, pontos = linha.split()
        notas.append(float(pontos))
    notas.sort()
    notas.reverse()

    print(notas[0])
    print(notas[1])
    print(notas[2])
