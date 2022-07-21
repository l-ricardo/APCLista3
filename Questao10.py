# Questao 10
def divisor_de_codigo(codigo):
    tamanho = len(codigo)-1
    j = 0
    while j < tamanho:
        if (codigo[j] in list('0123456789')) and (codigo[j+1] in list('ABCDEFGHIJKLMNOPRSTUVWXYZ')):
            codigo = codigo[:j+1] + ' ' + codigo[j+1:]
        j +=1
        tamanho = len(codigo)-1
    return (codigo.split())

linhas = int(input())
decodificado = ''
for i in range(linhas):
    letra_numero = divisor_de_codigo(input())
    for i in range(len(letra_numero)):
        decodificado += letra_numero[i][0]*int(letra_numero[i][1:])
    print(decodificado)
    decodificado = ''


# Teste                                                 # Resposta
# 2 / X1A10D10 / V20                                    # XAAAAAAAAAADDDDDDDDDD / VVVVVVVVVVVVVVVVVVVV