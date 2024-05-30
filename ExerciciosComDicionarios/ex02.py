"""Faça um programa, utilizando Dicionários, que peça para o usuário inserir o nome de três produtos de mercado e seus respectivos preços e os mostre na tela."""
dicionario={}
for c in range(3):
    chave=input(f"Produto {c+1}: ")
    valor=float(input(f"Valor do produto {c+1}: "))
    dicionario[chave]=valor
print(dicionario)