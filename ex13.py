gen=input("Qual seu genero?[H/M]").upper()
altura=float(input("Qual sua altura?"))

if gen=="H" :
    print(f"Seu peso ideal é {round(((72.7*altura) - 58),2)}")
else:
    print(f"Seu peso ideal é {round(((62.1*altura) - 47.7),2)}")

##Para homens: (72.7*h) - 58
##Para mulheres: (62.1*h) - 44.7S5
    