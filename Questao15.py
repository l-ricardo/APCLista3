# Questao 15
pa, pb, ta, tb = map(float,input().split())
ta /= 100
tb /= 100

if ta<tb or int(pa*ta)==0:
    print('A nunca alcancara B.')
else:
    anos = 0
    while pa < pb:
        pa += int(pa * ta)
        pb += int(pb * tb)
        anos += 1
        if anos == 1000:
            print('Mais de um milenio.')
            break
    if anos != 1000:
        print(f'Vai alcancar em {anos} ano(s).')
        

# Testes                               # Respostas
# 100 150 1.0 0                        # Vai alcancar em 50 ano(s).
# 90000 120000 5.5 3.5                 # Vai alcancar em 16 ano(s).
# 123 2000 2.0 3.0                     # A nunca alcancara B.