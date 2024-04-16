"""Altere o programa anterior, intercalando 3 vetores de 10 elementos cada."""
lista1=[]
lista2=[]
lista3=[]
lista4=[]
for c in range(10):
    x=int(input("Informe um valor para o primeiro vetor:"))
    lista1.append(x)
    x=int(input("Informe um valor para o segundo vetor:"))
    lista2.append(x)
    x=int(input("Informe um valor para o terceiro vetor:"))
    lista3.append(x)
    lista4.append(lista1[c])
    lista4.append(lista2[c])
    lista4.append(lista3[c])
print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")
print(f"Lista 3: {lista3}")
print(f"Lista 4 intercalando os elementos: {lista4}")