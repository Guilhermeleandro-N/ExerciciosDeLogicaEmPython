"""Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
Os juros e a quantidade de parcelas seguem a tabela abaixo:
Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
1       0
3       10
6       15
9       20
12      25
Exemplo de saída do programa:
Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
R$ 1.000,00     0               1                       R$  1.000,00
R$ 1.100,00     100             3                       R$    366,00
R$ 1.150,00     150             6                       R$    191,67"""
vpar=[]
juros=[]
montante=[]
tjuros=[0,0.10,0.15,0.2,0.25]
qpar=[1,3,6,9,12]
vlr=float(input("Qual o valor da dívida?"))
print("Valor da dívida/valor dos juros/quantidade de parcelas/valor das parcelas")
for c in range(5):
    montante.append(vlr*(1+tjuros[c]))
    juros.append(vlr*tjuros[c])
    vpar.append(montante[c]/qpar[c])
    print(f"R$ {montante[c]:.2f}\t\t// R${juros[c]:.2f}\t\t// {qpar[c]:.2f}\t\t//R${vpar[c]:.2f}")

