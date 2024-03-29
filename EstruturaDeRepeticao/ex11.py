"""Altere o programa anterior para mostrar no final a soma dos números."""
a=int(input("Me informe o primeiro numero:"))
b=int(input("Me informe o segundo número:"))
soma=0
if a>b:
    for x in range(a,b-1,-1):
        print(f"{x} ")
        soma+=x
elif b>=a:
    for x in range(a,b+1):
        print(f"{x} ")
        soma+=x
print(f"A soma desses valores é {soma}")