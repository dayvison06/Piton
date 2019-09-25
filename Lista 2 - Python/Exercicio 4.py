#Exercício 4: Faça um algoritmo que exiba a soma dos PARES e ÍMPARES compreendidos entre [10 99].

print('Código em Execução ....')


p = 10

for p in range(10, 99):

    if p % 2 == 0:
        print(f'Nº Par: {p}')

    elif p % 2 != 0:

        print(f'Nº Impar: {p}')
