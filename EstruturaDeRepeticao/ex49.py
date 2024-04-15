"""Faça um programa que mostre os n termos da Série a seguir:
  S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 
Imprima no final a soma da série."""
d=1
t=int(input("Quantos termos deverei informar e somar? "))
soma=0
for c in range(1,t+1):
    if c<(t):
        print(f" {c}/{d} +", end="")
        soma+=c/d
        d+=2
    else:
        print(f" {c}/{d} =", end="") 
        soma+=c/d
print(f" {soma:.2f}")
