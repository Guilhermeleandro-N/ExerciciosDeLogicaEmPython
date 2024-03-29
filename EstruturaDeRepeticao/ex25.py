"""Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada."""
soma=0
n=int(input("Quantos pessoas tem no grupo? "))
for c in range(n):
    idade=int(input("Informe uma idade: "))
    soma+=idade
media=soma/n
if media>=0 and media<=25:
    print(f"A idade media da turma é {media}.\nSão Jovens!")
elif media>=26 and media<=60:
    print(f"A idade media da turma é {media}.\nSão adultos!")
elif media>60:
    print(f"A idade media da turma é {media}.\São idosos!")