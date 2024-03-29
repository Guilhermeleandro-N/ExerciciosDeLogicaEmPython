"""Faça um programa que calcule o mostre a média aritmética de N notas."""
soma=0
n=int(input("Quantos notas você ira informar?"))
for c in range(n):
    nota=float(input("Informe uma nota:"))
    soma+=nota
media=soma/n
print(f"A media aritmetica das notas informadas é {media}.")