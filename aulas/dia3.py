# terça-feira, 27 de maio.
# Operadores Aritimeticos

# variáves
a =5
b = 2

print(a + b)
print(a * b)
print(a ** b)
print(a / b)
print(a == b)
print(a != b)

# ** exponecial
# // Divisão inteiro
# % Divisão com resto

print(a // b)
print(a / b)
print(a % b)
print(a ** b)

# Operadores de comparação

# variável
x = 10
y = 5

print(x > 5)
print(x < y)
print(x != y)
print(5 >= 5)
print(5 <= 1)

# Operadores Lógicos -> Unir comparacoes em cenarios mais complexos.
# AND, OR E NOT

# variárvel
idade = 50
possui_carteira = True
# Resolução aqui usei um operador logico and -> as proposições são verdadeiras
sou_habilitado = (idade >= 18) and possui_carteira
# empremir o resultado
print(f"eu tenho categoria D {sou_habilitado} motorista nota 10!")

# not = inverter um booleano

chovendo = True
nao_chovendo = not chovendo

print("chovendo", chovendo)
print('Não chovendo', nao_chovendo)


# if -> chovendo == false, not chovendo

# revisao 
# nota > 7 e frequencia > 80%

nota = 8
frequencia = 60

passou_de_ano = (nota > 7) and (frequencia > 80)

print("Passou de ano", passou_de_ano)

# senhas iguais
# criando um registro de usuario

senha = "teste123"
confirmacao_senha = "teste123"

if senha != confirmacao_senha:
    print("Digite a senha novamente")
else:
    print("Registro criado com sucesso!")


# if -> se eu estudo passo no concurso

estudo = "aprovado"
nao_estudei = "reprovado"

if estudo != nao_estudei:
    print("passei show")
else:
    print("Estude novamente") 

    

# if -> se eu estudo passo no concurso

estudou = input("Você estudou? (sim/não): ")

if estudou.lower() == "sim":
    print("Parabéns, você passou no concurso!")
else:
    print("Estude novamente para passar.")


