# Questao 02
def soma_harmonica(x):
    if x==1:
        return 1
    else:
        return 1/x + soma_harmonica((x-1))


# Testes                 # Respostas
print(soma_harmonica(6)) # 2.4499999999999997
print(soma_harmonica(5)) # 2.283333333333333
print(soma_harmonica(2)) # 1.5