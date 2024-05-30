"""Faça um programa, utilizando Dicionários, que peça para o usuário inserir quatro notas e mostre na tela as notas e a média entre elas."""
notas={}
media=0
for c in range(4):
    nota=float(input(f"nota {c+1}:"))
    notas[f"nota {c+1}"]=nota
print(notas)
for c in notas.values():
    media+=c
print(f"Medias das notas: {media}")