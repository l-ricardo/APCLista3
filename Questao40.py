# Questao 40
num = int(input())

if num==1:
    result = 'Faina'
elif num==2:
    result = 'Emidio'
else:
    for i in range(1, num-1):
        if num%i==0 and i!=1:
            result = 'Faina'
            break
        else:
            result = 'Emidio'

print(result)


# Testes       # Respostas
# 2            # Emidio
# 3            # Emidio
# 4            # Faina