"""Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas."""
aluno=[]
altura=[]
for c in range(10):
    vlr=int(input("Numero do estudante: "))
    aluno.append(vlr)
    vlr=float(input("Altura do aluno: "))
    altura.append(vlr)
    if c==0:
        maior=altura[c]
        menor=altura[c]
        pmaior=c
        pmenor=c
    else:
        if maior<altura[c]:
            maior=altura[c]
            pmaior=c
        if menor>altura[c]:
            menor=altura[c]
            pmenor=c
print(f"\t\t MAIOR ALUNO\nAluno: {aluno[pmaior]}\nAltura: {altura[c]}\n\t\t MENOR ALUNO\nAluno: {aluno[pmenor]}\nAltura: {altura[pmenor]}")