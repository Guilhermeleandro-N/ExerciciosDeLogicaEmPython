"""Faça um programa para imprimir:
    1
    1   2
    1   2   3
    .....
    1   2   3   ...  n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha."""
def loop(cont):
    for i in range(1,cont+1):
        print(f" {i} ", end="")
    print()

n=int(input("Quantas linhas crescente você deseja imprimir?"))
for c in range(1,n+1):
    loop(c)
    