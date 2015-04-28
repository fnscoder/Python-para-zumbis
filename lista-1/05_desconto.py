'''
Lista 1 - Exercício 5
Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.
Felipe Nogueira de Souza
@_outrofelipe
'''

preco = float(input('Informe o preço do produto: '))
desconto = float(input('Informe o percentual de desconto: '))
print ('O desconto foi de R$ %.2f' %(preco * desconto/100))
print ('O valor com desconto foi R$ %2.f' %(preco - (preco * desconto/100)))
