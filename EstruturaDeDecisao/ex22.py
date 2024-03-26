"""Faça um Programa que peça um número inteiro e determine se ele é par ou impar.
Dica: utilize o operador módulo (resto da divisão)."""
numero=int(input("Informe um número inteiro:\n"))
if (numero%2==1):
    print(f"O número {numero} é impar")
else:
    print(f"O número {numero} é par")