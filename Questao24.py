# Questao 24
k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())
feridos = 0
for i in range(1,d+1):
    if i%k==0 or i%l==0 or i%m==0 or i%n==0:
        feridos +=1
print(feridos)

# Testes                  # Respostas
# 1 / 2 / 3 / 4 / 12      # 12