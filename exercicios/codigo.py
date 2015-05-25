palavra = input("Digite uma palavra: ")
codigo = ''
for l in palavra:
    if l in 'aeiou':
        codigo += '*'
    else:
        codigo += l
print(codigo)
