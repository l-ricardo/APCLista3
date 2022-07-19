# Questao 04
def aprovacao(notas):
    p1,p2,p3 = map(float, notas.split())
    media = (p1+p2+p3)/3.00
    if media >= 7.00:
        return True
    else:
        return False

boletim_turma = []
tamanho_turma = int(input())
for i in range(tamanho_turma):
    boletim_turma.append(aprovacao(input()))

for i in range(len(boletim_turma)):
    if boletim_turma[i]:
        print(f'O ALUNO {i} FOI APROVADO')
    else:
        print(f'O ALUNO {i} FOI REPROVADO')

# Teste                                                  # Resposta
# 3 / 10.0 10.0 10.0 / 10.0 10.0 1.0 / 7.0 7.0 6.99      # O ALUNO 0 FOI APROVADO / O ALUNO 1 FOI APROVADO / O ALUNO 2 FOI REPROVADO