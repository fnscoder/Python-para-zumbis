'''
Lista 3 - Exercício 2
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao
nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
Felipe Nogueira de Souza
Twitter: @_outrofelipe
'''

user = input("Digite um nome de usuário: ")
password = input("Digite uma senha: ")

while user == password:
    print ("Erro! O usuário não pode ser igual a senha!")
    user = input("Digite um nome de usuário: ")
    password = input("Digite uma senha: ")
    
print ("Usuário: ", user)
print ("Senha: ", password)
