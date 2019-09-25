# Escreva um algoritmo que leia de 10.000 habitantes de uma pequena cidade se está empregado
# ou não e exiba em porcentagem a quantidade de empregados e desempregados desta pequena cidade.

# Armazenador
e = 0;  # Empregados
d = 0;  # Desempregados
p = 1;  # Valor inicial de Habitantes

# Quantidade de Habitantes
hab = int(input('Insira a Quantidade de Habitantes: '))

for h in range(0, hab):
    ler = int(input(f'Habitante {p} esta empregado? Digite 1-Sim 2-Não '))
    p += 1
    if ler == 1:
        e += 1
    else:
        d += 1

# Percentual
qe = e * 100 / hab
qd = d * 100 / hab

print(f'Quantidade de Empregados: {e} || Representando: {qe: .2f}% do Total ')
print(f'Quantidade de Desempregados: {d} || Representando: {qd: .2f}% do Total ')
