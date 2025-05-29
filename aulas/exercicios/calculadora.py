
# Peça ao usuário para inserir dois números e armazene-os em variáveis.
# Calcule a soma, subtração, multiplicação e divisão desses números.
# Exiba os resultados.

# Primeirio vamos colacar as vaviáveis
# Input -> é uma função permite que o usuário imprima dados.
# Float -> Usamos float()
#para converter a entrada em um número de ponto flutuante.

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo Número: "))

# aqui vou colocar a logíca da calculadora simples

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2
potenciacao = numero1**numero2

print("Soma: ", soma)
print("Subtracao: ", subtracao)
print("Multiplicacao: ", multiplicacao)
print("Divisao: ", divisao)
print("Potenciacao: ", potenciacao)