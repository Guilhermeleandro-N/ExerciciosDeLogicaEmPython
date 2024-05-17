"""Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721."""

def inverso(n,casa):
    soma=0
    contador=0
    for c in range(casa-1, -1, -1):
        x=int((n/(10**(c))))
        soma+=(x*(10**contador))
        y=(x*(10**c))
        n-=y
        contador+=1
    return soma
def contar(valor):
    y=1
    contador=0
    #funcao
    while True: 
        if (valor/y)>9:
            contador+=1
        elif (valor/y)<9:
            contador+=1
            break
        y*=10
    return contador


n=int(input("Me informe um valor que lhe mostrarei seu reverso: "))
print(inverso(n,contar(n)))
