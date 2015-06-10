def palindrome(palavra):
    print('É palímdrome') if palavra == palavra[::-1] else print('Não é palíndrome')

word = input ('Palavra: ')
palindrome(word)
