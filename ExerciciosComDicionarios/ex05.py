"""Faça um programa, utilizando Dicionários, que:
1° Passo: Peça para o usuário inserir o nome de três funcionários e os mostre na tela.
2° Passo: Peça para o usuário demitir um funcionário e mostre na tela os funcionários restantes.
"""
dicionario={}
for c in range(3):
    dicionario[c+1]=input(f"Funcionário {c+1}: ")
print(f"Funcionários: {dicionario}")
numb=int(input("Informe o número do funcionario que deseja demitir: "))
dicionario.pop(numb)
print(f"Funcionário restantes: {dicionario}")