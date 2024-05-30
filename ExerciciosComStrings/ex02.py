"""Nome ao contrário em maiúsculas. Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas. Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas."""
def maiusc(nome):
    NOME=[]
    for c in range(len(nome)-1,-1,-1):
        NOME.append(nome[c])
    NOME="".join(NOME)
    return NOME.upper()

nome=input("Nome: ")
print(maiusc(nome))

