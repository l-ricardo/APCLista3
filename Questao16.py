# Questao 16
n = int(input())
rei_gasta = 0
for i in range(n):
    dinheiro = int(input())
    if dinheiro<1000:
        rei_gasta += 1000 - dinheiro
print(rei_gasta)

# Teste                                                 # Resposta
# 1 / 990                                               # 10
# 2 / 999 / 1050                                        # 1
# 2 / 0 / 2000                                          # 1000