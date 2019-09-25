# Escrever um algoritmo para que calcule a média dos números múltiplos de 6 que se encontram no intervalo de [6,6𝑥].
# Onde 𝑥 é um (1) único número inteiro positivo (𝑥≥1), lido do usuário.

# Instrução
print('Calcule a média dos números múltiplos de 6 que se encontram no intervalo de 6 até 6 * (O valor Inserido)')

# Variável para realizar leitura de Entrada do Usuário
entrada = int(input('Insira o Número: '))

# Contador que armazenará a quantidade de múltiplos encontrados
contador = 0

# Variável que somará a sequência de múltiplos
soma = 0

for x in range(6, 6 * entrada):
    if x % 6 == 0:
        print(f'{x}')
        contador += 1
        soma = soma + x

# Somatória dos Valores
print(f'Somatória: {soma}')

# Fórmula para achar a média
med = soma / contador

print(f'Quantidade de Múltiplos: {contador}')
print(f'Média dos Múltiplos: {med}')
