palavra = input ('Palavra: ')
print('É palímdromo') if palavra == palavra[::-1] else print('Não é palíndromo')
