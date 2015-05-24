'''
Seja o statement sobre diversidade: “The Python Software Foundation and the global Python
community welcome and encourage participation by everyone. Our community is based on
mutual respect, tolerance, and encouragement, and we are working to help each other live up
to these principles. We want our community to be more diverse: whoever you are, and
whatever your background, we welcome you.”.
Seja o mesmo texto acima “splitado”. Calcule quantas palavras possuem uma das letras
“python” e que tenham mais de 4 caracteres. Não se esqueça de transformar maiúsculas para
minúsculas e de remover antes os caracteres especiais.
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
        if l in p and len(p) > 4:
            return True
    return False
    
lista = []
paragrafo = "The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you."
total = 0

paragrafo = limpa_txt(paragrafo)

for palavra in paragrafo:
    if verifica(palavra):
        lista.append(palavra)
        total += 1

print("Lista original: ", paragrafo)
print("\n\nA quantidade de palavras que contém uma das letras de python e mais de 4 caracteres e: ", total)
print("\n\nLista com palavras que tem uma das letras de python e mais de 4 caracteres: ", lista)
