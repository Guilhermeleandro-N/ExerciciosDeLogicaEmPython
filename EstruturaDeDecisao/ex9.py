#Faça um Programa que leia três números e mostre-os em ordem decrescente.
x=float(input("Me informe 3 números distintos\n"))
y=float(input(""))
z=float(input(""))
if x>y and x>z:
    print(f"{x}")
elif y>x and y>z:
    print(f"{y}")
elif z>x and z>y:
    print(f"{z}")

if (x>y and z>x ) or ( x>z and x<y ):
    print(f"{x}")
elif (y>x and y<z) or (y>z and y<x):
    print(f"{y}")
elif (z>x and z<y) or (z>y and z<x):
    print(f"{z}")


if x<y and x<z:
    print(f"{x}")
elif y<x and y<z:
    print(f"{y}")
elif z<x and z<y:
    print(f"{z}")