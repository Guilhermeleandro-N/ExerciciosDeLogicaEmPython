"""Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘. Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20. Se valores fora da faixa forem informados, eles devem ser modificados para valores dentro da faixa de forma elegante."""
def retangulo(comprimento,altura):
    for c in range(altura+2):
        if c==0 or c==altura+1:
            print(f"+{"-"*comprimento}+")
        else:
            print(f"|{" "*comprimento}|")

comprimento=int(input("Informe um valor inteiro para o comprimento(máximo 20): "))
if comprimento<1:
    comprimento=1
elif comprimento>20:
    comprimento=20
altura=int(input("Informe um valor para a altura(máximo 20): "))
if altura<1:
    altura=1
elif altura>20:
    altura=20
retangulo(comprimento,altura)