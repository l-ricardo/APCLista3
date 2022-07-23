# Questao 38
def zero_entre_um_nao(num):
    s = list(num)
    if len(s)==1 or len(s)==2 or not('1'in s):
        return '0'
    s_comeco = []
    s_meio = []
    s_fim = []
    for i in s:
        if not ('1'in s_comeco):
            s_comeco.append(i)
    for i in s:
        if i=='1':
            s_meio.append(i)
    for i in reversed(s):
        if not ('1'in s_fim):
            s_fim.append(i)
    s_fim.reverse()
    return str(len(s) - (len(s_comeco) + len(s_meio) + len(s_fim) - 2))

n = int(input())
respostas = []

for i in range(n):
    respostas.append(int(zero_entre_um_nao(input())))

for i in respostas:
    print(i)


# Teste                         # Resposta
# 3 / 010011 / 0 / 1111000      # 2 / 0 / 0