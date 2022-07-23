# Questao 30
n = int(input())
print('1 elefante incomoda muita gente...')
for i in range(1, n):
    print(f'{i+1} elefantes incomodam' + ', incomodam'*(i) + ' muito mais...')
    print(f'{i+1} elefantes incomodam muita gente...')

print(f'{n+1} elefantes incomodam' + ', incomodam'*(n) + ' muito mais...')



# Teste                            # Resposta
# 2                                 # 1 elefante incomoda muita gente...
                                    #/ 2 elefantes incomodam, incomodam muito mais...
                                    #/ 2 elefantes incomodam muita gente...
                                    #/ 3 elefantes incomodam, incomodam, incomodam muito mais...