# Escrever um algoritmo que leia vários Números 𝑁 (𝑢𝑚 𝑝𝑜𝑟 𝑣𝑒𝑧) que, no intervalo entre [10 90],
# divididos por 5 possuem resto 2. Exiba a soma dos números lidos, parando o programa para 𝑁=0.

# Variável para Somar os Valores
soma = 0

for x in range(10, 90):

    # Leitor de Dados, Número que é inserido
    ler = int(input('Digite um Número que dividido por 5, o resto é 2, Caso deseja Parar, Pressione 0: '))

    if ler % 5 == 2:
        print(f'O Número {ler} está Aprovado')
        soma = soma + ler


    elif ler > 0 and ler < 10:
        print('Erro Na Leitura, Porfavor Escolha Valores entre 10 a 90')

    elif ler == 0:
        print('Fim da Leitura')
        break

    else:
        print('O Número não é divisível por 5 ou resto não = 2')

# Soma dos Valores
print(f'Somatória dos Números Lidos: {soma}')
