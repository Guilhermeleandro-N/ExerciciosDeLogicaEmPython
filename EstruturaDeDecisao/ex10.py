#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

letra=input("Em que turno você estuda?[M/V/N]\n").upper()
if (letra=="M" or letra=="V" or letra=="N"):
    if (letra=="M"):
        print("Bom Dia!")
    elif (letra=="V"):
        print("Boa Tarde!")
    elif (letra=="N"):
        print("Boa noite")
else:
    print("Valor inválido.")