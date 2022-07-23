# Questao 19
def fibonacci(x):
    if x==0:
        return 0
    elif x==1:
        return 1
    else:
        return fibonacci(x-2) + fibonacci(x-1)


# Testes                  # Respostas
print(fibonacci(0))       # 0
print(fibonacci(1))       # 1
print(fibonacci(10))      # 55