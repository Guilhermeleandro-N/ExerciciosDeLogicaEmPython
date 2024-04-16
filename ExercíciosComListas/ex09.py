"""Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor."""
lista=[]
soma=0
for i in range(10):
    x=int(input("Informe um valor inteiro: "))
    lista.append(x)
    soma+=x**2
print(f"Os valores informados são: {lista}\nA soma dos quadrados do vetor: {soma}.\n")