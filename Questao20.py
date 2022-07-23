# Questao 20
def fibonacci(n):
    t1 = 0
    t2 = 1
    if n==1:
        sequencia = '0'
    else:
        sequencia = '0 1'
        for i in range(n-2):
            t3 = t1 + t2
            sequencia += ' ' + str(t3)
            t1 = t2
            t2 = t3
    print(sequencia)


# Testes                  # Respostas
fibonacci(2)              # 0 1
fibonacci(1)              # 0
fibonacci(10)             # 0 1 1 2 3 5 8 13 21 34