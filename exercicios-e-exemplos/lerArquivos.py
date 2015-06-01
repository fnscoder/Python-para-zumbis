arquivo = open('numeros.txt', 'r')
for linha in arquivo.readlines():
    print(linha.rstrip())    #rstrip() retira caracteres de controle do lado direito da string
arquivo.close()
