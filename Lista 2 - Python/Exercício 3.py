#Exercício 3: Escrever um algoritmo em Python para exibir os múltiplos de ƞ compreendidos
#  entre o intervalo:
#  [𝐿𝑖𝑚𝑖𝑡𝑒𝐼𝑛𝑓𝑒𝑟𝑖𝑜𝑟 𝐿𝑖𝑚𝑖𝑡𝑒𝑆𝑢𝑝𝑒𝑟𝑖𝑜𝑟] ϵ ℕ. Sendo que:
#✓ {ƞ ∈ ℕ/ ƞ ≥ 2}
#✓ {𝐿𝑖𝑚𝑖𝑡𝑒𝐼𝑛𝑓𝑒𝑟𝑖𝑜𝑟 , 𝐿𝑖𝑚𝑖𝑡𝑒𝑆𝑢𝑝𝑒𝑟𝑖𝑜𝑟 ∈ ℕ/ 𝐿𝑖𝑚𝑖𝑡𝑒𝑆𝑢𝑝𝑒𝑟𝑖𝑜𝑟 ≥ 𝐿𝑖𝑚𝑖𝑡𝑒𝐼𝑛𝑓𝑒𝑟𝑖𝑜𝑟}

n = int(input('Digite um valor maior ou igual a 2:'))

for i in range (n,11*n):
    if i % n == 0:
        print(f'{i}')