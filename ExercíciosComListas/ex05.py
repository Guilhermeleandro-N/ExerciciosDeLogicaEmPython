"""Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores."""
numb=[]
numpar=[]
numimpar=[]
for c in range(20):
    x=int(input("Informe um valor inteiro: "))
    numb.append(x)
    if x%2==0:
        numpar.append(x)
    else:
        numimpar.append(x)
print(f"Os 20 valores inciais: {numb}")
print(f'Desses valores, esses são os pares :{numpar}')
print(f"E esses são os ímpares: {numimpar}")
            