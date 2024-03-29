"""Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação."""
x=int(input("Deseja fazer a simulação quantas vezes?"))
for i in range(0,x):  
    a=float(input("Qual o tamanho da população A?\n"))
    at=float(input("Qual a taxa de crescimento da população A(EM %)?\n"))
    b=float(input("Qual o tamanho da população B?\n"))
    bt=float(input("Qual a taca de crescimento da população b?(EM %)?\n"))
    at=at/100
    bt=bt/100
    c=0
    while a<b:
        c+=1
        a=a*(1+at)
        b=b*(1+bt)
    print(f"Foram necessários {c} anos.")