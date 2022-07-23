# Questao 26
n = int(input())
soma_x = 0
soma_y = 0
soma_z = 0
for i in range(n):
    vetor = list(map(int,input().split()))
    soma_x += vetor[0]
    soma_y += vetor[1]
    soma_z += vetor[2]
if soma_x==0 and soma_x==0 and soma_x==0:
    print('YES')
else:
    print('NO')

# Testes                                # Respostas
# 3 / 4 1 7 / -2 4 -1 / 1 -5 -3         # NO