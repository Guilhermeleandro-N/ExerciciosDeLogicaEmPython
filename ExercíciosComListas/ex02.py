"""Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa."""
lista=[]
for c in range(10):
    x=int(input("Informe um valor inteiro: "))
    lista.append(x)
lista.reverse()
print(lista)