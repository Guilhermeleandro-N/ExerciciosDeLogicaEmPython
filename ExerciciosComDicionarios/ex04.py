"""Faça um programa, utilizando Dicionários, que:
1° Passo: Peça para o usuário inserir quatro coisas em uma “Caixa Misteriosa” .
2° Passo: Peça para o usuário inserir um número.
3° Passo: Mostre na tela o que foi inserido na posição do número inserido pelo usuário."""
dicionario={}
print("CAIXA MISTERIOSA")
for c in range(4):
    valor=input("Insira: ")
    dicionario[f"chave {c+1}"]=valor
numb=int(input("Digite um valor: "))
lista=list(dicionario.keys())
print(f"O {dicionario[lista[numb-1]]} está na caixa misteriosa na posição {numb}")

