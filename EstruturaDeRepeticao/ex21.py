"""Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1."""
n=int(input("Me informe um número e eu lhe direi se ele é primo ou não."))
cont=0
for c in range(1,n+1):
    if n%c==0:
        cont+=1
if cont>2:
    print(f"{n} não é primo!")
else:
    print(f"{n} é primo!")
