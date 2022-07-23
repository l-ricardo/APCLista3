# Questao 17
n, ingresso = map(int, input().split())
dinheiro = 0

for i in range(n):
    dinheiro += int(input())

media = dinheiro/n
print(f'media: {int(media)}')

if ingresso<media:
    print('o rock reinara mais uma vez')
else:
    print('rockeiros trabalhando ja')


# Testes                                         # Respostas
# 6 300 / 350 / 300 / 300 / 230 / 400 / 300      # media: 313 / o rock reinara mais uma vez
# 3 150 / 150 / 150 / 149                        # media: 149 / rockeiros trabalhando ja