"""Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0."""

cont=0
lista=[[],[],[],[],[],[],[],[],[],[],]

for c in range(10):
    soma=0
    media=0
    print(f"{c+1}° aluno:")
    for i in range(4):
        x=float(input(f"Qual foi a {i+1}ª nota do aluno? "))
        lista[c].append(x)
        soma+=x
        if i==3:
            media=soma/4
            lista[c].append(round(media,2))

for c in range(10):
    if lista[c][4]>=7:
        cont+=1
    print(f"Media do {c+1}° aluno: {lista[c][4]}")
print(f"{cont} alunos tiveram media igual ou superior a 7.")


    

