"""Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo."""
cont=0

a=b=c=d = 0
while True:
    vlr=float(input("INFORME UM VALOR: "))
    if vlr<0:
        break
    cont+=1
    if vlr>=0 and vlr<=25:
        a=+1
    elif vlr>=26 and vlr<=50:
        b+=1
    elif vlr>=51 and vlr<=75:
        c+=1
    elif vlr>=76 and vlr<=100:
        d+=1
print(f"Quantidade de números informados nos intervalors:\n[0-25]: {a}\n[26-50]: {b}\n[51-75]: {c}\n[76-100]: {d}")