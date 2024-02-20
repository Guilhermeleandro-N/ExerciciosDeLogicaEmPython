#1 litro = 3 metros
#Cada lata 18 liros=54 metos =80 R$
tmhtotal=(float(input("Quantos metros quadrados precisam ser pintados?\n")))
divint=tmhtotal//54
divmod=tmhtotal%54
if divmod != 0:
    divint+=1

print(f"Você vai precisar de {divint} balde(s) de tinta(s) que custam {round((divint*80),2)} R$.")