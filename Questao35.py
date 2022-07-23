# Questao 33
num = list(input())
if num[0]!='-':
    print(int(''.join(reversed(num))))
else:
    print(int('-'+''.join(reversed(num[1:]))))


# Testes                                                # Respostas
# 2084                                                  # 4802
# -3831                                                 # -1383
# 54                                                    # 45