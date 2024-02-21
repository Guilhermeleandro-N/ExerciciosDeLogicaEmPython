pesopeixes=float(input("Quantos quilos de peixe pescou hoje?"))
excesso=int(0)
multa=int(0)
if pesopeixes>50:
    excesso=float(pesopeixes-50)
    multa=float(excesso*4)

print(f"Voce pescou {round(pesopeixes,2)} quilos de peixe.\nO excesso foi de {round(excesso,2)}.\nA multa que deve ser paga é {round(multa,2)}.")
