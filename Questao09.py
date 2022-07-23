# Questao 09
linhas = int(input())
x = 0

for i in range(linhas):
    operacao = input()
    if operacao == 'X++' or operacao == '++X':
        x +=1
    else:
        x -=1

print(x)


# Testes                   # Respostas
# 1 / ++X                  # 1
# 2 / X++ / --X            # 0
# 3 / ++X / ++X / ++X      # 3