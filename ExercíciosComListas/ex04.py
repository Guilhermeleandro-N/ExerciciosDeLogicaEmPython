"""Faça um Programa que leia um vetor de 10 caracteresor e diga quantas consoantes foram lidas. Imprima as consoantes."""
lista=[]
consoantes=[]
cont=0
for c in range(10):
    while True:
        x=input("Digite um único caratere: ")
        x=x.lower()
        if len(x)==1:
            break
        else:
            print("Digite um único caractere!")
    lista.append(x)
    if lista[c] in {"b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"} :
        consoantes.append(lista[c])
        cont+=1
print(f"Foram infomadas {cont} consoantes:")
print(consoantes)



    