"""Faça um programa que leia 5 números e informe a soma e a média dos números."""
for x in range(1,6):
    a=float(input("Me informe um valor:\n"))
    if x==1:
        soma=a
    else:
        soma+=a
media=soma/5
print(f"A soma dos 5 valores infomados é {soma}\nA média dos 5 valores informados é {media}")
    