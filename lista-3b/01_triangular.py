'''
Lista 3b - Exercício 1
Dizemos que um número natural é triangular se ele é produto de três números naturais
consecutivos. Exemplo: 120 é triangular, pois 4.5.6 = 120. Dado um inteiro não-negativo n,
verificar se n é triangular.
Felipe Nogueira de Souza
Twitter: @_outrofelipe
'''

n = int(input('Informe um número natural: '))
i = 1
p = 0

while p < n:
    p = i * (i + 1) * (i + 2)        
    i += 1
if p == n:
    print ('O número %d é triangular, pois %d * %d * %d = %d' %(n, i - 1, i, i + 1, n))
else:
    print ('O número %d não é truangular' %n)

    
