import urllib.request
pagina = urllib.request.urlopen(
    'http://beans.itcarlow.ie/prices-loyalty.html')
texto = pagina.read().decode('utf-8')
onde = texto.find('>$')
inicio = onde + 2
fim = onde + 4
preco = texto[inicio:fim]
print(preco)
