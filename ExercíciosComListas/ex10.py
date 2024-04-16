"""Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores."""
lista1=[]
lista2=[]
lista3=[]
for c in range(10):
    x=int(input("Informe um valor para o primeiro vetor:"))
    lista1.append(x)
    x=int(input("Informe um valor para o segundo vetor:"))
    lista2.append(x)
    lista3.append(lista1[c])
    lista3.append(lista2[c])
print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")
print(f"Lista 3 intercalando os elementos: {lista3}")