"""Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos."""
cont=0
soma=0
media=0
lista=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
for c in range(30):
        x=int(input(f"Idade do {c+1}° aluno:"))
        lista[c].append(x)
        x=float(input(f"Altura do {c+1}° aluno:"))
        lista[c].append(x)
        soma+=lista[c][1]
media=round((soma/30),2)
for c in range(30):
    if lista[c][1]<media and lista[c][0]>13:
          cont+=1
print(f"Existem {cont} alunos com mais de 13 anos com a altura abaixo da média({media})")
        
