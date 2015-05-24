'''
Seja o statement sobre diversidade: “The Python Software Foundation and the global Python
community welcome and encourage participation by everyone. Our community is based on
mutual respect, tolerance, and encouragement, and we are working to help each other live up
to these principles. We want our community to be more diverse: whoever you are, and
whatever your background, we welcome you.”. Gere uma lista de palavras deste texto com
split(), a seguir crie uma lista com as palavras que começam ou terminam com uma das letras
“python”. Imprima a lista resultante. Não se esqueça de remover antes os caracteres especiais
e cuidado com maiúsculas e minúsculas.
Autor: Felipe Nogueira de Souza
'''
def limpa_txt(texto):
    texto = texto.lower()
    texto = texto.replace('.', '')
    texto = texto.replace(',', '')
    texto = texto.replace(':', '')
    texto = texto.split()
    return texto

def verifica(p):
    for l in 'python':
        if p.startswith(l) or p.endswith(l):
            return True
    return False
    
lista = []
paragrafo = "The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you."

paragrafo = limpa_txt(paragrafo)

for palavra in paragrafo:
    if verifica(palavra):
        lista.append(palavra)

print("Lista original: \n", paragrafo)
print("\n\nLista com iniciadas ou terminadas com uma das letras de python: \n", lista)
