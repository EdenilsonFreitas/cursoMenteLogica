"""
1. Calculando o Troco
Você foi a uma padaria e comprou alguns itens:
● Pão: R$3.50
● Leite: R$4.20
● Café: R$2.80
Você pagou com uma nota de R$20. Calcule quanto de troco você deve receber.
"""
"""
pao = 3.50
leite = 4.20
cafe = 2.80

#compra_total = pao + leite + cafe
compra_total = ["pao","leite","cafe"] # usando array para somar

valor_pago = 20

troco = valor_pago - compra_total

print("Valor da compra :", compra_total)
print("Valor a receber :", troco)
"""
# Usando array para somar essa lista
pao = 3.50
leite = 4.20
cafe = 2.80

# Lista com os valores dos produtos
compra_total = [pao, leite, cafe]  

# Somando os valores da lista com a função sum()
soma_total = sum(compra_total)

valor_pago = 20

troco = valor_pago - soma_total

print("Valor da compra :", soma_total)
print("Valor a receber :", troco)

