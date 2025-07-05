# Condicionais -> estruturas if, else
#idade = 18

# estrutura do if => if COMPARAÇAO

# O bloco do if, só executado se a condição for verdadeira
#if idade >= 18:
    #print("Você é maior de idade")

# else
# é executado em casos onde o if não executa

#if idade >= 18:
   # print("Você é maior de idade")
#else:
    #print("Você é MENNOR de idade")    

# meia entrada => menor de 18 anos ou estaja estudando em escola publica / faculdade
"""
idade = 17
estuda_rede_publica = False

if idade < 18 or estuda_rede_publica:
    print("Tem direito a meia entrada")
"""
"""
nota: A, B C
> 9 = A, > 8 = B, > 6 =C
elif => else if
é uma condiçao intermediaria entre if e else
"""
"""
nota = 6.1
if nota > 9:
    print("o seu conceito é A")
elif nota > 8:
    print("o seu conceito é B")
elif nota > 6:
    print("seu conceito é C") 
else:
    print("Voce precisa melhorar seu conceito")           
"""
# climas: ensolarado, chuvoso, nublado
"""
clima = "chuvoso"

if clima == "ensolarado":
    print("o dia está ensolarado")
elif clima == "nublado":
    print("o dia está nublado")
elif clima == "chuvoso":  
    print("o dia está chuvoso")   
"""
# vendas 
# > 1000 = .5%
# > 500 = 1%
# = 2%
"""
venda =250

if venda > 1000:
    comissao = venda * 0.005
    print("A comissão de venda foi: ", comissao)
elif venda > 500:
    comissao = venda * 0.01
    print("A comissão de venda foi: ", comissao)
else:
    comissao = venda * 0.02
    print("A comissão de venda foi: ", comissao)
"""

# baseado numa entrada de usuario se o numero é maior ou menor que zero
# funçao input
numero  = float(input("Digite um numero: "))

if numero > 0:
    print("o numero é maior que 0", numero)
else:
    print("o numero é menor que zero", numero)  
"""
Como requisito para um emprestimo. Para ser aprovado, voce precisa ter renda comparavada e nao ter restriçoes no nome.
"""
renda_aprovada = True
nao_ter_restricoes = True

emprestimo_aprovado = renda_aprovada and nao_ter_restricoes

print("Vou pegar o dinheiro", emprestimo_aprovado)
