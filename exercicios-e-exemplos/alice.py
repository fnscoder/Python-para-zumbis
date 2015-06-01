arq = open('alice.txt')
texto = arq.read()
texto = texto.lower()
import string
for c in string.punctuation:
    texto = texto.replace(c, ' ')
texto = texto.split()

dic = {}
for p in texto:
    if p not in dic:
        dic[p] = 1
    else:
        dic[p] += 1
palavra = input('Informe a palavra: ')
print('A palavra: %s aparece %s vezes no texto' %(palavra, dic[palavra]))
arq.close()
