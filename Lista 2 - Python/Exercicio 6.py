# Escreva um algoritmo que leia o salário em reais (R$) de 1000 clientes de um shopping e exiba na tela
# , em porcentagem, a divisão dos clientes por tipo: A, B ou C, conforme a seguir:
# ✓ A: Maior ou igual a 15 Salários Mínimos ou
# ✓ B: Menor que 15 Salários Mínimos ou maior ou igual a 5 Salários Mínimos ou
# ✓ C: Menor que 5 Salários Mínimos.
# Declarar o Salário Mínimo (SM: R$ 998.05).

# Valor do Salário Mínimo
salMinimo = 998.05

# Contador para Organizar os Clientes
contclient = 0

# Contador para Organizar os Tipos de Cliente
a = 0
b = 0
c = 0

# Limite de Cliente a ser Inserido
limitec = int(input('Insira a Quantidade de Cliente a ser Pesquisado (Ex: 10): '))

for x in range(0, limitec):
    contclient += 1
    salario = float(input(f'Insira o Salário do Cliente {contclient} em R$: '))
    if salario >= (salMinimo * 15):
        print('Cliente Tipo A ')
        a += 1
    elif salario < (salMinimo * 15) and salario >= (salMinimo * 5):
        print('Cliente Tipo B')
        b += 1

    else:
        print('Cliente Tipo C')
        c += 1

# Cálculo para extrair a porcentagem dos Clientes de cada Tipo
# Percentual A
perca = a * 100 / limitec
# Percentual B
percb = b * 100 / limitec
# Percentual C
percc = c * 100 / limitec

print(f'Total de Tipos de Clientes:')
print(f'A = {a} Cerca de {perca: .1f}%')
print(f'B = {b} Cerca de {percb: .1f}%')
print(f'C = {c} Cerca de {percc: .1f}%')
