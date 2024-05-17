"""Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo."""
def p_ou_n(valor):
    if valor>0:
        print("P")
    elif valor<0:
        print("N")
    else:
        print("0 é um valor neutro.")

n=float(input("Me informe um valor real. Se o valor for positivo, imprimira 'P', se for negativo, imprimira 'N'.\nValor: "))
p_ou_n(n)


