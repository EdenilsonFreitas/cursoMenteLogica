

#paulo quer comprar um sorvete com 4 bolas em uma sorveteria que possui tres sabores de sorvete: chocalate, morango e uva. De quantas modos diferentes ele pode fazer a compra?


import math

# Dados do problema
sabores = 3
bolas = 4

# Fórmula da combinação com repetição
modos_diferentes = math.comb(sabores + bolas - 1, bolas)

print(f"Paulo pode escolher o sorvete de {modos_diferentes} diferentes formas.")

