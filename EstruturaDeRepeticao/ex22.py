"""Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível."""
n=int(input("Me informe um número e eu lhe direi se ele é primo ou não."))
cont=0
div=[]
for c in range(1,n+1):
    if n%c==0:
        cont+=1
        div.append(c)
if cont>2:
    print(f"{n} não é primo! e é divisível pelos seguintes números: {div}")
else:
    print(f"{n} é primo!")
