"""Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
Fatorial de: 5
5! =  5 . 4 . 3 . 2 . 1 = 120"""
n=int(input("Fatorial de: "))
fatorial=1
for c in range (1,n+1):
    fatorial*=c
print(f"{n}! = ", end="")
for c in range (n,0,-1):
    if c>1:
        print(f" {c} .", end="")
    else:
        print(f" {c} ", end="")
print(f"= {fatorial}")

