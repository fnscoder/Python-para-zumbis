from random import randint
print ('Bem vindo!')
secreta = randint(1, 100)
tentativa = 0
while True:
    chute = int(input('Chute um número: '))
    tentativa += 1
    if chute == secreta:
        print ('Parabéns! Você acertou o número %d na %dª tentativa'
               %(secreta, tentativa))
        break
    else:
        print ('Alto' if chute > secreta else 'Baixo')
print ('Fim do jogo!')
