# Questao 33
pontuacao = list(map(int,input().split()))
pontuacao.pop()
print(*reversed(pontuacao))


# Testes                                    # Respostas
# 1 2 -1                                    # 2 1
# 1 2 3 4 5 6 7 8 9 10 11 12 13 -9999       # 13 12 11 10 9 8 7 6 5 4 3 2 1 
# 3 3 3 3 3 -3                              # 3 3 3 3 3