"""Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos."""
#Modifiquei um pouco o problema para usar listas dentro da função
lista=[]
def somavalores(valores):
    soma=0
    for c in valores:
        soma+=c
    return soma

qtd=int(input("Quantos valores deseja informar?"))
print(f"Informe {qtd} valores que lhe entregarei a soma deles! ")

for c in range(qtd):
    n=int(input(f"Valor {c+1}: "))
    lista.append(n)

print(f"A soma dos valores informados é {somavalores(lista)}")