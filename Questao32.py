# Questao 32
soma = 0
n_provas = 0
while(True):
    nota = int(input())
    if nota != -1:
        soma += 1/nota
        n_provas += 1
    else:
        print(int(n_provas//soma))
        break

# Testes                                                # Respostas
# 9 / 7 / 10 / -1                                       # 8
# 5 / 3 / -1                                            # 3
# 4 / 5 / 12 / 4 / 99 / -1                              # 6