"""Faça um Programa que leia 4 notas, mostre as notas e a média na tela."""
lista=[]
soma=0
for c in range(4):
    x=int(input(f"Informe a {c+1} nota:"))
    lista.append(x)
    soma+=lista[c]
print("A soma de ", end="")
for c in range(4):
    if c<4:
        print(f"{lista[c]} + ", end="")
    elif c==4:
        print(f"{lista[c]} ", end="")
print(f"= {soma}\nE a media é {soma/4}")
