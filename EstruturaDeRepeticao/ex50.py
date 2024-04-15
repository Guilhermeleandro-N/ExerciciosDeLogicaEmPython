"""Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos."""
soma=0
n=int(input("Quantos termos você deseja imprimir e somar? "))
for c in range(1,n+1):
    if c==1:
        print(f'1 +', end="")
    elif c<n:
        print(f" {1}/{c} +", end="")
    else:
        print(f" {1}/{c} = ", end="")
    soma+=1/(c)
print(soma)
