"""Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

Compara duas strings
String 1: Brasil Hexa 2006
String 2: Brasil! Hexa 2006!
Tamanho de "Brasil Hexa 2006": 16 caracteres
Tamanho de "Brasil! Hexa 2006!": 18 caracteres
As duas strings são de tamanhos diferentes.
As duas strings possuem conteúdo diferente."""
frase1=input("Me informe a primeira string: ")
frase2=input("Me informe a segunda string: ")

print(f"Primera string: {frase1}")
print(f"Segunda string: {frase2}")
print(f"Tamanho de '{frase1}':{len(frase1)} caracteres")
print(f"Tamanho de '{frase2}':{len(frase2)} caracteres" )
if len(frase1)==len(frase2):
    print("As duas strings são de tamanhos iguais.")
else:
    print("As duas strings são de tamanhos diferentes.")
if frase1==frase2:
    print("As duas string possuem conteúdo igual.")
else:
    print("As duas frases possuem conteúdos diferentes.")
