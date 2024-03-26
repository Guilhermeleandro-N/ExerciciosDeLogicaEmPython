"""
Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
"""
morango=float(input("Quantos kg de morango você quer comprar?\n"))
if morango<=5:
    precom=morango*2.5
elif morango>5:
    precom=morango*2.2
maca=float(input("Quantos kg de maçã você quer comprar?\n"))
if maca<=5:
    precoma=maca*2.2
elif maca>5:
    precoma=maca*1.5
precototal=precom+precoma
if (precototal>25) or (morango+maca>8):
    precototal=precototal*0.9
print(f"O valor a ser pago por {morango} kg de morango e {maca} kg de maçã é {round(precototal,2)}R$")    