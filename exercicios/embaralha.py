def embaralha(palavra):
    import random
    palavra = input("Digite uma palavra: ")
    palavra = list(palavra)
    random.shuffle(palavra)
    return ''.join(palavra)

print(embaralha('teste'))
