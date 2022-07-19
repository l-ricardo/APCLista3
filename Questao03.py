# Questao 03
n = int(input())
vetu = list(map(int,input().strip().split()))[:n]
vetv = list(map(int,input().strip().split()))[:n]
# print('testando')
# print(n)
# print(vetu)
# print(vetv)
provet = 0
for termou in vetu:
    for termov in vetv:
        provet = provet + termou*termov
    print(provet)

# Testes                                       # Respostas
# 4  /  3 -4 2 5         /  1 1 1 1            # ortogonais
# 3  /  -2 0 1           /  1 2 -2             # -4
# 8  /  1 0 1 0 1 0 1 0  /  0 1 0 1 0 1 0 1    # ortogonais