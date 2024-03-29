"""Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números ímpares."""
lista = []
par=0
impar=0
for c in range (10):
    numero=int(input("Informe um número inteiro:\n"))
    lista.append(numero)
for c in range(10):
    if lista[c]%2==0:
        par+=1
    else:
        impar+=1
print(f"Foram informados {par} numeros pares e {impar} numeros ímpares.")