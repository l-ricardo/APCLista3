# Questao 01
def anobissexto(ano):
    if (ano%4==0 and ano%100!=0) or ano%400==0:
        return 'Sim'
    else:
        return 'Nao'

# Testes                 # Respostas
print(anobissexto(2020)) # Sim
print(anobissexto(2021)) # Nao
print(anobissexto(2100)) # Nao
