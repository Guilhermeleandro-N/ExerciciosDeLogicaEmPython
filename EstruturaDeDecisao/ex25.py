"""Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente"."""
resposta=input("Telefonou para a vitima?")
cont=0
if resposta[0]=="S" or resposta[0]=="s":
    cont+=1
resposta=input("Esteve no local do crime?")
if resposta[0]=="S" or resposta[0]=="s":
    cont+=1
resposta=input("Mora perto da vítima?")
if resposta[0]=="S" or resposta[0]=="s":
    cont+=1
resposta=input("Devia para a vítima?")
if resposta[0]=="S" or resposta[0]=="s":
    cont+=1
    resposta=input("Já trabalhou com a vítima?")
if resposta[0]=="S" or resposta[0]=="s":
    cont+=1

if cont==2:
    print("Investigado suspeito.")
elif cont==3 or cont==4:
    print("Investigado é cúmplice.")
elif cont==5:
    print("Investigado é culpado.")
else:
    print("O investigado é inocente")