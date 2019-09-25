# Exercício 1: Múltiplos des 3

print('Conheça os Múltiplos de 3')
i = 0
bau = 0
while i <= 100:
    if i % 3 == 0:
        bau += 1
        print(f'{i} é Múltiplo de 3')
    i += 1

print(f'Quantidade de múltiplos de que existe de 0 á 100: {bau} ')