# Questao 08
senha = list(input())
tamanho_certo = False
tem_maiuscula = False
tem_minuscula = False
tem_numero = False
tem_ponto = False
if len(senha) > 5 and len(senha) < 37:
    tamanho_certo = True
for i in range(len(senha)):
    if senha[i] in list('abclefghijklmnopqrstuvwxyz'):
        tem_maiuscula = True
    if senha[i] in list('ABCDEFGHIJKLMNOPRSTUVWXYZ'):
        tem_minuscula = True
    if senha[i] in list('0123456789'):
        tem_numero = True
    if senha[i] in list(' ,.;:^~`´!@#$%¨&*'):
        tem_ponto = True

if tamanho_certo and tem_maiuscula and tem_minuscula and tem_numero and not tem_ponto:
    print('Senha valida.')
else:
    print('Senha invalida.')

# Teste                                       # Resposta
# AbcdEfgh99                                  # Senha valida.
# Aass9                                       # Senha invalida.
# Aassd9                                      # Senha valida.