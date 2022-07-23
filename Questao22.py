# Questao 22
def pattern(n):
    if n%5==0:
        fator = (n//5)
    else:
        fator = (n//5)+1

    for i in range(fator):
        print(n)
        n -= 5
    for i in range(fator+1):
        print(n)
        n += 5


# Testes        # Respostas
pattern(16)     # 16 / 11 / 6 / 1 / -4 / 1 / 6 / 11 / 16
pattern(10)     # 10 / 5 / 0 / 5 / 10
pattern(3)      # 3 / -2 / 3