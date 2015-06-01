'''
Programa de xemplo utilizando a criptografia de Cesar Desenvolvido por uma aluna de 12 anos
'''

def esconde(msg):
    s = ''
    for c in msg: s += chr(ord(c) + 30000)
    return s

def mostra(msg):
    s = ''
    for c in msg: s += chr(ord(c) - 30000)
    return s

mensagem = input("Digite uma mensagem: ")

print("Mensagem codificada: ", esconde(mensagem))

mensagem = input("Digite a mensagem para decodificar: ")

print("Mensagem decodificada: ", mostra(mensagem))
