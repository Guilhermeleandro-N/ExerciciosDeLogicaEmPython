#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
letra=input("Escreva uma letra:\n")
if (ord(letra)>64 and ord(letra)<91) or (ord(letra)>96 and ord(letra)<123):
    if letra=="a"or letra=="e" or letra=="i" or letra=="o" or letra=="u":
        print(f"A letra {letra} é uma vogal.")
    else:
        print(f"A letra {letra} é uma consoante.")
else:
    print("Caractere inválido.")
