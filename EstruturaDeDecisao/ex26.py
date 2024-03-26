"""Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90."""
litros=float(input("Qual a quantidade de litros que você deseja abastercer?\n"))
tipo=input("Qual o tipo de combustível?(G-gasolina ou A=álcool)\n").upper()
if tipo=="A":
    if litros<=20:
        preco=(litros*1.90)*0.97
    elif litros>20:
        preco=(litros*1.90)*0.95
    print(f"O valor por {litros} litros de álcool é {round(preco,2)}")
elif tipo=="G":
    if litros<=20:
        preco=(litros*2.5)*0.96
    elif litros>20:
        preco=(litros*2.5)*0.94
    print(f"O valor por {litros} litros de gasolina é {round(preco,2)}")
