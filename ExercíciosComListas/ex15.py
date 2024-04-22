"""Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
Mostre a quantidade de valores que foram lidos;
Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
Calcule e mostre a soma dos valores;
Calcule e mostre a média dos valores;
Calcule e mostre a quantidade de valores acima da média calculada;
Calcule e mostre a quantidade de valores abaixo de sete;
Encerre o programa com uma mensagem;"""
notas=[]
menor_media=[]
maior_media=[]
soma=0
cont=0
print("Informe o valor -1 para encerrar a inserção de notas!\n")
while True:
    x=float(input("Me informe uma nota: "))
    x=round(x,2)
    if x==-1:
        break
    notas.append(x)
    cont+=1
    soma+=x
media=round((soma/cont),2)
for c in notas:
    print(f"|{c}", end="")
print()
for c in range(cont-1,-1,-1):
    print(f"|{notas[c]}|", )

print(f"A soma dos valores é: {soma}")
print(f"A media dos valores é: {media}")
conti=0
contii=0
for c in notas:
    if c<media:
        menor_media.append(c)
        conti+=1
    elif c>media:
        maior_media.append(c)
        contii+=1
print(f"Numero de notas abaixo da media: {conti}")
if len(menor_media)>0:
    print(menor_media)
print(f"Numero de notas acima da media: {contii}")
if len(maior_media)>0:
    print(maior_media)
print("FIM DO PROGRAMA!!!")
