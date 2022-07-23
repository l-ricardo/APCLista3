# Questao 29
n = int(input())
resolver = 0
for i in range(n):
    saber = list(map(int,input().split()))
    if sum(saber)>1:
        resolver += 1
print(resolver)

# Testes                            # Respostas
# 3 / 1 1 0 / 1 1 1 / 1 0 0         # 2