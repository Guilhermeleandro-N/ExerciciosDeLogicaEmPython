"""Faça um Programa que leia um vetor de 5 números inteiros e mostre-os."""
lista=[]
for c in range(5):
    x=int(input("Informe um valor inteiro: "))
    lista.append(x)
for c in range(5):
    print(f"{lista[c]} ", end='')