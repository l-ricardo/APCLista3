# Questao 27
def ehPrimo(num):
    if num==1:
        result = 0
    elif num==2:
        result = 1
    else:
        for i in range(1, num-1):
            if num%i==0 and i!=1:
                result = 0
                break
            else:
                result = 1
    return result

def divisoresPrimos(num):
    result = 0
    for i in range(2, num-1):
        if num%i==0 and ehPrimo(i)==1:
            result += 1
    return result


# Testes                    # Respostas
print(ehPrimo(3))           # 1
print(ehPrimo(4))           # 0
print(ehPrimo(5))           # 1
print(ehPrimo(6))           # 0
print(divisoresPrimos(4))   # 1
print(divisoresPrimos(6))   # 2
print(divisoresPrimos(8))   # 1
print(divisoresPrimos(9))   # 1
print(divisoresPrimos(10))  # 2