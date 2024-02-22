#Faça um Programa que leia três números e mostre o maior e o menor deles.
#Faça um Programa que leia três números e mostre o maior deles.
x=float(input("Me informe 3 números distintos\n"))
y=float(input(""))
z=float(input(""))
if x>y and x>z:
    print(f"{x} é o maior")
elif y>x and y>z:
    print(f"{y} é o maior")
elif z>x and z>y:
    print(f"{z} é o maior")

if x<y and x<z:
    print(f"{x} é o menor")
elif y<x and y<z:
    print(f"{y} é o menor")
elif z<x and z<y:
    print(f"{z} é o menor")