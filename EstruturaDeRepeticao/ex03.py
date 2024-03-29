"""Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';"""
while True:
    nome=input("Insira seu nome:\n")
    if len(nome)>3:
        break
    else:
        print("Seu nome tem que ter mais do que três caracteres!")
while True:
    idade=int(input("Qual sua idade?\n"))
    if idade>=0 and idade <=150:
        break
    else:
        print("Você tem que ter entre 0 e 150 anos.")
while True:
    salario=float(input("Qual o seu salário?\n"))
    if salario>0:
        break
    else:
        print("Você tem que ter um salário!")
while True:
    sexo=input("Qual seu sexo?[F/M]\n").upper()
    if sexo=="F" or sexo=="M":
        break
    else:
        print("Apenas [F/M] é aceito nesse questionario.")