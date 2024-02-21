#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
genero=input("Qual seu genero?[F/M]").upper()
if genero=="F":
    print(f"F - feminino")
else:
    if genero=="M":
        print("M - masculino")
    else:
        print("Resposta invalida")
