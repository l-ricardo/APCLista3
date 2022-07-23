# Questao 28
pontos = list(map(int,input().split()))
print(min(pontos),pontos.index(min(pontos)))
print(max(pontos),pontos.index(max(pontos)))
print(*pontos)


# Testes                  # Respostas
# 10 555 8 444 659        # 8 2 / 659 4  / 10 555 8 444 659