"""Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas."""
def soma_imposto(custo, taxa):
    soma=custo*(1+taxa)
    return soma
custo=float(input("Qual o valor do produto sem impostos? "))
taxa_imposto=(float(input("Qual a taxa de imposto? (Em %) ")))/100
valor_total=soma_imposto(custo, taxa_imposto)
print(f"O valor do produto com impostos é {round(valor_total,2)} R$.")
