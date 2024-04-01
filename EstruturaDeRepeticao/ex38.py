"""Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário."""
#Modifiquei a questão por achar mais interessante dessa maneira
salario=float(input("Qual o salário inicial do funcionário? "))
tx=0.015
ano=int(input("Começou a trabalhar em que ano?"))
anoa=int(input("Estamos em que ano? "))
for c in range(anoa-ano):
    salario+=salario*(tx*c)
print(f"O salário atual do funcionário é {salario:.2f}")