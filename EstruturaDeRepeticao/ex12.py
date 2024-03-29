"""Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
Tabuada de 5:
5 X 1 = 5
5 X 2 = 10
...
5 X 10 = 50"""
while True:
    x=int(input("De que numero você deseja ver a tabuada?"))
    if x>=1 and x<=10:
        break
for c in range(1,11):
    print(f"{x} x {c} = {x*c}")