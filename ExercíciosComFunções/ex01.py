""""Faça um programa para imprimir:
    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha."""
def imprimir(qtd):
    for c in range(1,n+1):
        print(f" {c} "*c)
n=int(input("Quantas linhas crescente você deseja imprimir?"))
imprimir(n)
