"""Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido."""
nota=-1
while nota<0 or nota>10:
    nota=float(input("Me de uma nota:"))
    if nota<0 or nota>10:
        print("Nota inválida")
    elif nota>=0 and nota <=10:
        print("Nota válida")
