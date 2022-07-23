# Questao 25
def ppa(a,b):
    if (a==3 and b==1) or (a==3 and b==2) or (a==1 and b==2):
        return 'Jogador 1 venceu'
    elif (a==1 and b==3) or (a==2 and b==1) or (a==2 and b==3):
        return 'Jogador 2 venceu'
    elif a==2 and b==2:
        return 'Ambos venceram'
    elif a==1 and b==1:
        return 'Sem ganhador'
    else:
        return 'Aniquilacao mutua'
   
        
# Testes                    # Respostas
print(ppa(1, 1))            # Sem ganhador
print(ppa(1, 2))            # Jogador 1 venceu
print(ppa(1, 3))            # Jogador 2 venceu
print(ppa(2, 2))            # Ambos venceram