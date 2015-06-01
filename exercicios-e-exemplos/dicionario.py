d = {}
d['a'] = 'alpha'
d['o'] = 'omega'
d['g'] = 'gama'
print(d)
print(d['a'])
print(d['o'])
print(d['g'])

#posso pegar as keys
print(d.keys())

#ou os valores
print(d.values())

letra = input('Informe uma letra: ')

#pergunto se está no dict
if letra in d:
    print('%s está no dicionario' %letra)
else:
    print('%s não está no dicionario' %letra)

#quando faço for no dict pego a chave
for chave in d:
    print(chave)

#for para imprimir os valores

for chave in d:
    print(d[chave])
