"""Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento."""
import math
numero=float(input("Me informe uma número\n"))
decimal=math.modf(numero)
print(decimal[0])
if (decimal[0]!=0):
    print(f"{numero} é um numero decimal")
else:
    print(f"{numero} é um número inteiro")
