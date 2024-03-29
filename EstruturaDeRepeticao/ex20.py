"""Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16."""
v=int(input("Quantos fatoriais deseja calcular?"))
for a in range(v):
    while True:
        n=int(input("Que número deseja calcular o fatorial?\n"))
        if n>=0 and n<=16:
            break
        else:
            print("Só se pode calcular o fatorial de números inteiros positivos e menores que 16.")
    fatorial=1
    for c in range (1,n+1):
        fatorial*=c
    print(f"O fatorrial de {n} é {fatorial}")