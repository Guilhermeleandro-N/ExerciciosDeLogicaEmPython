"""Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16"""
number=int(input("Me diga um valor inteiro menor que 1000:\n"))
numero=int(number)
centenas=int(numero/100)
numero=int(numero%100)
dezenas=int(numero/10)
numero=int(numero%10)
unidades=int(numero)
if (number<1000):
    if (centenas==0) and (dezenas==0) and (unidades==0):
        print(f"0.")
    elif (centenas!=0) and (dezenas==0) and (unidades==0):
        print(f"{centenas} centenas.")
    elif (centenas!=0) and (dezenas!=0) and (unidades==0):
        print(f"{centenas} centenas e {dezenas} dezenas.")
    elif (centenas!=0) and (dezenas!=0) and (unidades!=0):
        print(f"{centenas} centenas, {dezenas} dezenas e {unidades} unidades")
    elif (centenas==0) and (dezenas!=0) and (unidades!=0):
        print(f"{dezenas} dezenas e {unidades} unidades")
    elif (centenas==0) and (dezenas==0) and (unidades!=0):
        print(f"{unidades} unidades.")
else:
    print("Número inválido.")
        
