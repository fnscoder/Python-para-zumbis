n = int(input("Informe a quantidade de caracteres: "))
caracteres = []
consoantes = 0
i = 1
while i <= n:
    c = input("Informe o %d caracter: " %i)
    caracteres.append(c)
    i += 1
i = 0
while i < n:
    if caracteres[i] not in "aeiou":
        consoantes += 1
    i += 1
print("O total de consoantes eh: ", consoantes)
