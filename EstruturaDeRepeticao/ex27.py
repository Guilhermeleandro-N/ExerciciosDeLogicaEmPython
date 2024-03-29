"""Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos."""
n=int(input("Existem quantas turmas? "))
soma=0
for c in range(1,n+1):
    while True:
        alunos=int(input(f"Qual o número de alunos na turma {c}? "))
        if alunos<=40 and alunos>=0:
            break
        else:
            print("O número de alunos por turma deve ser entre 0 e 40!")
    soma+=alunos
media=soma/n
print(f"A media de alunos por turma é {media}.")

