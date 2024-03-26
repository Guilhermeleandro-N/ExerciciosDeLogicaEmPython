#Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
#Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
#Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
#Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
import math
print("Olá, sou uma calculadora de equações de segundo grau!\nMe informe os valores que lhe direi as raizes!")
a=float(input("A:\n"))
if a!=0:
    b=float(input("B:\n"))
    c=float(input("C:\n"))
    delta=((b**2)-4*a*c)
    deltasqr=float(math.sqrt(delta))
    if delta<0:
        print("A equação não existe raízes reais.")
    elif delta==0:
        x1=(-b+deltasqr)/(2*a)
        print(f"Só existe uma raíz, que é: {round(x1,2)}")
    elif delta>0:
        x1=((-b)+deltasqr)/(2*a)
        x2=((-b)-deltasqr)/(2*a)
        print(f"Existem duas raízes reais:\nX1:{round(x1,2)}\nx2: {round(x2,2)}")

