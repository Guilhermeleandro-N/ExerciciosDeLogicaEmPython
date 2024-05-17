"""Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado."""
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
x=int(input("Me informe um valor inteiro que eu lhe direi a quantidade de dígitos que ele possui\nValor: "))
print(f"O número de dígitos que esse número possui é: {contar(x)}")
