#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
x=float(input("Me informe o preço de 3 produtos\n"))
y=float(input(""))
z=float(input(""))

if x<y and x<z:
    print(f"Você deve comprar o produto que tem o valor: {x} R$.")
elif y<x and y<z:
    print(f"Você deve comprar o produto que tem o valor: {y} R$.")
elif z<x and z<y:
    print(f"Você deve comprar o produto que tem o valor: {z} R$.")