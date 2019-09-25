# Um marca de sucos que saber a opinião dos seus clientes sobre três diferentes novos “mix” de sabores.
# As degustações e votação se realizaram num supermercado durante certo período.
# Faça um algoritmo em Python, que exiba a porcentagem dos clientes que gostaram da opção:
# 1: Mix 1
# , 2: Mix 2
# ou 3: Mix 3 de sabores.
# Pare o algoritmo quando for digitada a opção zero (0).

# Varíavel do mix
m1 = 0
m2 = 0
m3 = 0

while True:

    # Ler Votação: Variável para Inserir valor.
    ler = int(input('Qual Mix você prefere?:'
                    ' Digite 1 (Mix 1) , 2 (Mix 2) , 3 (Mix 3) ou'
                    ' Digite 0 para parar a votação. Seu Voto: '))

    if ler == 0:
        print('Votação Finalizada, Resultados da Votação:')
        break

    elif ler == 1:
        m1 += 1

    elif ler == 2:
        m2 += 1

    else:
        m3 += 1

# Somador de Votos, para saber quantos votos ao total foram realizados
somav = (m1 + m2 + m3)

# Cálculo Percentual da Votação
calm1 = m1 * 100 / somav
calm2 = m2 * 100 / somav
calm3 = m3 * 100 / somav

# Saída dos Votos
print(f' Mix 1:  {m1} Votos')
print(f' Mix 2:  {m2} Votos')
print(f' Mix 3:  {m3} Votos')

# Saída Total dos Votos
print(f'Total de Votos: {somav}')

#Saída Percentual dos Votos
print(f'Mix 1, Votação Representa {calm1: .1f}% do Total')
print(f'Mix 2, Votação Representa {calm2: .1f}% do Total')
print(f'Mix 3, Votação Representa {calm3: .1f}% do Total')

