"""Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações."""
nome="o"
senha="o"
while nome==senha:
    nome=input("Nome de usuário:")
    senha=input("Senha:")
    if nome==senha:
        print("O nome e a senha não podem ser iguais!")
    

