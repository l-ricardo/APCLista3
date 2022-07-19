# Questao 06
numero_voltas = int(input())
tempos = list(map(int, input().split()))
t_minimo = min(tempos)
diferenca = []
for i in range(numero_voltas):
    diferenca.append(str(tempos[i]-t_minimo))
print(' '.join(diferenca))

# Teste                                       # Resposta
# 5 / 20 15 23 17 16                          # 5 0 8 2 1