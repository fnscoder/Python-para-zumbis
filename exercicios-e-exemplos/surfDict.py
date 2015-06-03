'''f = open('surf.txt')
for linha in f:
    print(linha.strip())  #o .strip retira o caracter de controle que faz pular linha (/n)
f.close()'''
notas = {}
with open('surf.txt') as f:
    for linha in f:
        nome, pontos = linha.split()
        notas[float(pontos)] = nome
    for nota in sorted(notas, reverse = True):
        print('%s tem Nota: %4.2f' %(notas[nota], nota))
