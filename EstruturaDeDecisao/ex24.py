"""Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal."""
x=float(input("Me informe o primeiro valor:\n"))
y=float(input("Me informe um segundo valor:\n"))
operacao=input("Qual a operação que deseja realizar entre esses dois valores?[+,-,*,/,%]\n")
if(operacao=="+"):
    result=x+y
    print(f"O resultado da soma é {result}.")
elif(operacao=="-"):
    result=x-y
    print(f"O resultado da subtração é {result}.")
elif(operacao=="*"):
    result=(x*y)
    print(f"O resultado da multiplicação é {round(result,2)}.")
elif(operacao=="/"):
    result=round((x/y),2)
    print(f"O resultado da divisão de {x} por {y} é {round(result,2)}.")
elif(operacao=="%"):
    result=(x%y)
    if (result%1==0):
        result=int(result)
        print("O modulo de {x} e {y} é {result}")
    else:
        print("O modulo de {x} e {y} é {result}")
if(result%2==0):
    print("É um número par")
else:
    print("É um número impar")

if (result>0):
    print("É um número positivo")
elif(result==0):
    print("É um número neutro em relação a polaridade")
elif(result<=0):
    print("É um número negativo")

if (result%1==0):
    print("É um número inteiro")
else:
    print("É um número decimal")

