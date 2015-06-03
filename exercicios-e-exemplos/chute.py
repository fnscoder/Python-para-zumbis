from random import randint
print ('Bem vindo!')
sorteado = randint(1, 100)
chute = 0
while chute != sorteado:
    g = input('Chute um número: ')
    chute = int(g)
    if chute == sorteado:
        print ('Você venceu!')
    else:
        if chute > sorteado:
            print ('Alto')
        else:
            print ('Baixo')
print ('Fim do jogo!')
