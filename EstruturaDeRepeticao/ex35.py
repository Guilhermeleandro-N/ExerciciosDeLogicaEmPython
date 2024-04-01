"""Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário."""
b=int(input("Me informe um número e eu lhe mostrarei todos os números primos de 1 até ele: "))
for n in range(1,b+1):
    cont=0
#verifica se é primo
    for c in range(1,n+1):
        if n%c==0:
            cont+=1
    if cont<=2:
        print(f"{n} ", end="")
        