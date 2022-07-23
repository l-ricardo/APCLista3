# Questao 38
# n = int(input())
s = list(input())
contador = 0
repeticoes = len(s) - 1
for i in range(repeticoes):
    if s[i]=='1' and s[i+1]=='0' and ('1' in s[i:]):
        print(s)
        s.pop(i+1)
        contador += 1
        repeticoes += 1
print(contador)


# Testes                                                # Respostas
# 3 / 010011 / 0 / 1111000                              # 2 / 0 / 0