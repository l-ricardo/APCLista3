# Questao 37
n = int(input())
s = list(input())

for i in range(n):
    if i!=n-1:
        if s[i] == max(s[i],s[i+1]) and s[i]!=s[i+1]:
            s.pop(i)
            break
    else:
        s.pop(n-1)
        
print(''.join(s))


# Testes                              # Respostas
# 3 / aaa                             # aa
# 5 / abcda                           # abca
# 4 / abcd                            # abc
# 26 / lolthisiscoolfreehackforya     # llthisiscoolfreehackforya