# Questao 12
n_voltas = int(input())
tempos = list(map(int,input().split()))
t_max = max(tempos)
diferencas = ''
for i in range(n_voltas):
    diferencas += str(t_max-tempos[i]) + ' '
print(diferencas)

# Teste                                                 # Resposta
# 5  / 20 15 23 17 16                                   # 3 8 0 6 7