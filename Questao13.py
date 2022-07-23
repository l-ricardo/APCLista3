# Questao 13
alunos = 0
soma = 0

while(True):
    nota = int(input())
    if nota != -1:
        soma += nota
        alunos += 1
    else:
        print(soma//alunos)
        break


# Testes                         # Respostas
# 9 / 7 / 10 / -1                # 8
# 5 / -1                         # 5
# 4 / 5 / 12 / 4 / 99 / -1       # 24