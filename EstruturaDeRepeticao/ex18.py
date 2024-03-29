"""Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores."""
lista = []
n=int(input("Quantos números você ira informar?"))
for c in range(n):
    a=float(input("Informe um número:"))
    lista.append(a)
for c in range(n):
    if c==0:
        maior=lista[0]
    elif lista[c]>lista[c-1]:
        maior=lista[c]
print(f"O maior número informado foi {maior}.")
for c in range(n):
    if c==0:
        menor=lista[0]
    elif lista[c]<lista[c-1]:
        menor=lista[c]
print(f"O menor número informado foi {menor}.")
soma=0
for c in range(n):
    soma+=lista[c]
print(f"A soma dos números informados é {soma}")


    
