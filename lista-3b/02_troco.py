'''
Lista 3b - Exercício 2
Indique como um troco deve ser dado utilizando-se um número mínimo de notas. Seu
algoritmo deve ler o valor da conta a ser paga e o valor do pagamento efetuado desprezando
os centavos. Suponha que as notas para troco sejam as de 50, 20, 10, 5, 2 e 1 reais, e que
nenhuma delas esteja em falta no caixa.
Felipe Nogueira de Souza
Twitter: @_outrofelipe
'''

c = int(input('Informe o valor da conta: '))
p = int(input('Informe o valor do pagamento: '))

if c == p:
    print ('Não há troco')
elif c > p:
    print ('Pagamento insuficiente')
else:
    t = p - c
    cinquenta = t / 50
    t = t % 50

    vinte = t / 20
    t = t % 20

    dez = t / 10
    t = t % 10

    cinco = t / 5
    t = t % 5

    dois = t / 2

    um = t % 2

    print ('Quantidade de notas - TROCO')
    print ('Notas de R$ 50,00: %d \nNotas de R$ 20,00: %d \nNotas de R$ 10,00: %d \nNotas de R$ 05,00: %d \nNotas de R$ 02,00: %d \nNotas de R$ 01,00: %d' %(cinquenta, vinte, dez, cinco, dois, um))
