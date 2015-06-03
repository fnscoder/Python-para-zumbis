import urllib.request
pagina = urllib.request.urlopen(
    'http://beans.itcarlow.ie/prices.html')
texto = pagina.read().decode('utf-8')
preco = texto[234:238]
print(preco)
