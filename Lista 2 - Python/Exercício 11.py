# Escrever um algoritmo em que o usuário entre com um número inteiro qualquer
# {ƞ ∈ ℤ} e exiba na tela os 50 números subseqüentes ao que foi digitado pelo usuário.

#Entrada do Número
ler = int(input('Insira o número: '))
contador = 0

while contador <= 50:
    if ler >= 0 or ler <= 0:
        print(f'Nº: {ler}')
        ler += 1
        contador += 1
