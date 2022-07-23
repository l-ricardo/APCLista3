# Questao 14
n1, n2 = map(int,input().split())
divisores = []

for i in range(max(n1,n2)):
    if n1%(max(n1,n2)-i)==0 and n2%(max(n1,n2)-i)==0:
        divisores.append(max(n1,n2)-i)

if max(divisores)==1:
        print('Sao co-primos.')
else:
    print('Nao sao co-primos!')
  
    
# Testes         # Respostas
# 4 9            # Sao co-primos.
# 4 8            # Nao sao co-primos!
# 20 21          # Sao co-primos.