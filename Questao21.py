# Questao 21
n = int(input())

for i in range(n):
    if i==0:
        continue
    elif i%15==0:
        print('Fizz Buzz')
    elif i%3==0:
        print('Fizz')
    elif i%5==0:
        print('Buzz')
    else:
        print(i)


# Teste    # Resposta
# 6        # 1 / 2 / Fizz / 4 / Buzz / Fizz