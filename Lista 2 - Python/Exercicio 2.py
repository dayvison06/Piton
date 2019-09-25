# Exercicio 2:

# Escrever um algoritmo para exibir os múltiplos de 11, a soma e a média dos múltiplos de 
# 11, em ordem decrescente (inversa), compreendidos entre o intervalo: [200 100].

print('Rodando código ...')

soma = 0
i = 200
multiplos = 0

while i > 100:
    if i % 11 == 0:
        multiplos += 1
        soma += i
        print(f'{i} é Múltiplo de 11')
    i -= 1

media = soma / multiplos

print(f'Total de Múltiplos = {multiplos}')
print(f'Soma do Total = {soma}')
print(f'A Média dos Múltiplos de 11 = {media: .0f}')
