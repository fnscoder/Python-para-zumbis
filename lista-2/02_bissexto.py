'''
Lista 2 - Exercicio 2.
Determine se um ano é bissexto. Verifique no Google como fazer isso...
'''
ano = int(input('Informe o ano: '))

if ((ano % 400) == 0) or (((ano % 4) == 0) and (ano % 100) != 0):
    print ('O ano e bissexto')
else:
    print ('O ano NAO e bissexto')






    
