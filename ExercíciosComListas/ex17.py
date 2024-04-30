""""Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será determinado pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
Atleta: Rodrigo Curvêllo
 
Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m"""


while True:
    lista=[]
    soma=0
    nome=input("Atleta: ")
    if nome=="":
        break
    x=float(input("Primeiro salto: "))
    lista.append(x)
    x=float(input("Segundo salto: "))
    lista.append(x)
    x=float(input("Terceiro salto: "))
    lista.append(x)
    x=float(input("Quarto salto: "))
    lista.append(x)
    x=float(input("Quinto salto: "))
    lista.append(x)
    lista.sort()
    soma=lista[1]+lista[2]+lista[3]
    media=round((soma/3),2)
    print(f"""Melhor salto:  {lista[4]} m
Pior salto: {lista[0]} m
Média dos demais saltos: {media} m

Resultado final:
{nome}: {media} m""")