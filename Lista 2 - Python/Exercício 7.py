# Escrever um algoritmo que conte e soma todos os números ímpares que são múltiplos
# de três e NÃO múltiplos de 5 que se encontram no intervalo [9 90].
# Exiba a Contagem e a Soma destes números.

# Contador de múltiplos de três e não múltiplos de 5
contador = 0

# Variável que somará todos os múltiplos impressos na saída
soma = 0

for x in range(9, 90):
    if x % 3 == 0 and x % 5 != 0 and x % 2 != 0:
        print(f'Número: {x}')
        contador += 1
        soma = soma + x

print(f'Total de Múltiplos de 3 (Não PAR e Não Múltiplo de 5: {contador}')
print(f'Soma Total dos Múltiplos : {soma}')
