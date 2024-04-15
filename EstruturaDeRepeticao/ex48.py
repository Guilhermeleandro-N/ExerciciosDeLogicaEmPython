"""Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
Exemplo:
  12376489
  => 98467321"""
x=int(input("Me informe um número que eu lhe mostrarei ele de trás para frente!\nNúmero: "))
while True:
    if x>=1:
        casa=int(x%10)
        x=x/10
        print(f"{casa}", end="")
    else:
        break
