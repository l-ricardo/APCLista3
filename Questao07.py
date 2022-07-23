# Questao 07
cotacao = float(input())
tamanho = int(input())
quantidade = int(input())
total = cotacao*tamanho*1.025

for n_lote in range(quantidade):
    print(f'Lote: {n_lote+1} - Total da venda: R$ {total:.2f}')


# Teste                     # Resposta
# 4.20 / 1000 / 2           # Lote: 1 - Total da venda: R$ 4305.00 / Lote: 2 - Total da venda: R$ 4305.00