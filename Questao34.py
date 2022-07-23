# Questao 34
tamanho_certo = None
pe_do_bill = int(input())
chinelos = list(map(int,input().split()))
chinelos.sort()

for i in chinelos:
    if i>=pe_do_bill:
        tamanho_certo = i
        break

if tamanho_certo != None:
    print(chinelos.index(tamanho_certo))
else:
    print(-1)


# Testes                 # Respostas
# 30 / 32 40 35 37       # 0
# 34 / 30 38 32 28       # 3
# 30 / 29                # -1