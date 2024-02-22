#Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
n=int(input("Me diga um número correspondente a um dia da semana:\n"))
n-=1
if n>=0 and n<=6:
    dias=("Domingo!","Segunda","Terça!","Quarta!","Quinta!","Sexta!","Sabado!")
    print(dias[n])
else:
    print("Valor invalido!")