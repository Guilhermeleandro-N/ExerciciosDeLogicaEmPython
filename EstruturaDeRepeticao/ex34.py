"""Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo."""
#Mesma atividade do exercicio 21
n=int(input("Me informe um número e eu lhe direi se ele é primo ou não."))
cont=0
for c in range(1,n+1):
    if n%c==0:
        cont+=1
if cont>2:
    print(f"{n} não é primo!")
else:
    print(f"{n} é primo!")
