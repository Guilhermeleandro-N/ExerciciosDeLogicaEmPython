"""Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1."""
#1, 5, 10, 50, 100
number=int(input("Me diga o valor do saque(10 a 600):\n"))
numero=number
nt100=int(numero/100)
numero=int(numero%100)
nt50=int(numero/50)
numero=int(numero%50)
nt10=int(numero/10)
numero=int(numero%10)
nt5=int(numero/5)
numero=int(numero%5)
nt1=int(numero)
if(number>=10) and (number<=600):
    if(nt100>0):
        print(f"({nt100}) nota(s) de cem reais")
    if(nt50>0):
        print(f"({nt50}) nota(s) de cinquenta reais")
    if(nt10>0):
        print(f"({nt10}) nota(s) de dez reais")
    if(nt5>0):
        print(f"({nt5}) nota(s) de cinco reais")
    if(nt1>0):
        print(f"({nt1}) notas(s) de um real")
else:
    print("Valor de saque inválido.")