# Questao 03
n = int(input())
vet_u = list(map(int,input().strip().split()))[:n]
vet_v = list(map(int,input().strip().split()))[:n]
provet = 0

for i in range(n):
    provet += vet_u[i]*vet_v[i]
    
if provet==0:
    print('ortogonais')
else:
    print(provet)


# Testes                                       # Respostas
# 4  /  3 -4 2 5         /  1 1 1 1            # ortogonais
# 3  /  -2 0 1           /  1 2 -2             # -4
# 8  /  1 0 1 0 1 0 1 0  /  0 1 0 1 0 1 0 1    # ortogonais