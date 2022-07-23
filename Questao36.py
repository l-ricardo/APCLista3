# Questao 36
def remove_duplicatas(lista):
    result = []
    for i in range(len(lista)):
        if not(lista[i] in result):
            result.append(lista[i])
    return result


# Testes                                       # Respostas
print(remove_duplicatas([1,2,2,3]))            # [1, 2, 3]
print(remove_duplicatas([1,1,1]))              # [1]
print(remove_duplicatas([0,0,1,1,2,2,3,3]))    # [0, 1, 2, 3]