# Questao 05
datagrama = list(map(int,input().split()))
d = 0

for i in range(len(datagrama)-1):
    for j in range(len(datagrama)-1-i):
        if datagrama[j]>datagrama[j+1]:
            datagrama[j], datagrama[j+1] = datagrama[j+1], datagrama[j]
            d += 1

print(d)


# Testes              # Respostas
# 1 4 5 9 15          # 0
# 1 5 2 3 4           # 3
# 1 5 2 4 3           # 4