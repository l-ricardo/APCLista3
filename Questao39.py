# Questao 39
mapa = list(input())
mapa.append('.')
tiros = 0

for i in range(len(mapa)):
    if mapa[i]=='o' and mapa[i+1]=='.':
        tiros += 1
        
print(tiros)


# Testes                           # Respostas
# ..o....oooo...oo..o.             # 4
# oooo.....ooooo..o.o.o            # 5
# oo.oo.o.o.oooo..o..ooo           # 7