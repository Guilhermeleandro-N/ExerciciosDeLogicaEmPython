"""Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números."""
lista=[]
soma=0
mult=1
for i in range(5):
    x=int(input("Informe um valor inteiro: "))
    lista.append(x)
    soma+=x
    mult*=x
print(f"Os valores informados são: {lista}\nA soma entre eles: {soma}.\nA multiplicação entre eles; {mult}")
    