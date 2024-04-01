"""Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário, conforme exemplo abaixo:
Montar a tabuada de: 5
Começar por: 4
Terminar em: 7

Vou montar a tabuada de 5 começando em 4 e terminando em 7:
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
Obs: Você deve verificar se o usuário não digitou o final menor que o inicial."""
while True:
    a=int(input("Montar a tabuada de: "))
    if 0<a<11:
        break
    else:
        print("Insira um valor entre 1 e 10.")
while True:
    b=int(input("Começar por: "))
    c=int(input("Terminar em: "))
    if (0<b<11 and 0<c<11) and b<c:
        break
    else:
        print("Insira dois valores entre 1 e 10, sendo o primeiro maior que o segundo.")
for e in range(b,c+1):
    print(f"{a} x {e} = {a*e}")

