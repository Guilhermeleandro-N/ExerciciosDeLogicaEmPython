"""Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem."""
base=int(input("Qual a base?\n"))
expoente=int(input("Qual o expoente?\n"))
for x in range(1,expoente+1):
    if x==1:
        resposta=base
    else:
        resposta*=base
print(f"{base} elevado a {expoente} é: {resposta}")