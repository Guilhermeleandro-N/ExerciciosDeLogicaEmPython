"""Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um."""
n=int(input("Quantos CD'S você tem? "))
soma=0
for c in range(1,n+1):
    valor=float(input(f"Quanto você pagou pela CD de número {c}? "))
    soma+=valor
media=soma/n
print(f"O valor total gasto em CD's é {soma}.\nO valor medio de cada CD é {media}.\n")