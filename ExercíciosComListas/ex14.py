"""Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente"."""
lista=[]
cont=0
while True:
    x=input("Telefonou para a vítima?[S/N] ")
    x=x.upper()
    if x!="S" and x!="N":
        print("Resposta inválida")
    else:
        break
lista.append(x)


while True:
    x=input("Esteve no local do crime?[S/N] ")
    x=x.upper()
    if x!="S" and x!="N":
        print("Resposta inválida")
    else:
        break
lista.append(x)

while True:
    x=input("Mora perto da vítima?[S/N] ")
    x=x.upper()
    if x!="S" and x!="N":
        print("Resposta inválida")
    else:
        break
lista.append(x)

while True:
    x=input("Devia para a vítima?[S/N] ")
    x=x.upper()
    if x!="S" and x!="N":
        print("Resposta inválida")
    else:
        break
lista.append(x)
while True:
    x=input("Já trabalhou com a vítima?[S/N] ")
    x=x.upper()
    if x!="S" and x!="N":
        print("Resposta inválida")
    else:
        break
lista.append(x)

for c in range(5):
    if lista[c]=="S":
        cont+=1
if cont==2:
    print("Suspeita")
elif cont==4 or cont==3:
    print("Cúmplice")
elif cont==5:
    print("Culpado")
else:
    print("Inocente")