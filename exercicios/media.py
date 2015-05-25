i = 0
total = 0
alunos = int(input("Informe a quantidade de alunos: "))
while i < alunos:
    nota = float(input("Informe a nota do %d aluno: " %(i+1)))
    total += nota
    i += 1
media = total/(alunos)
print("A média é %.2f" %media)
