"""Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120"""
n=int(input("Sou uma calculadora de fatorial!\nQue número deseja calcular o fatorial?\n"))
fatorial=1
for c in range (1,n+1):
    fatorial*=c
print(f"O fatorrial de {n} é {fatorial}")