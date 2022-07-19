# Questao 07
cotacao = float(input())
tamanho = int(input())
quantidade = int(input())
total = cotacao*tamanho*1.025
for n_lote in range(quantidade):
    print(f'Lote: {n_lote+1} - Total da venda: R$ {total:.2f}')