import os
os.system('cls')

# Questao 38
# n = int(input())
s = list(input())
s_novo = []
for i in range(len(s)-2):
    # if s[i]=='1':
    #     s_novo.append(s[i])
    if s[i]=='0' and ('1' in s[i-1:]) and ('1' in s[:i-1]):
        s.pop(i)
        print(s)
        #s_novo.append(s[i])
# print(''.join(s_novo))
# print(len(s)-len(s_novo))


# Testes                                                # Respostas
# 3 / 010011 / 0 / 1111000                              # 2 / 0 / 0