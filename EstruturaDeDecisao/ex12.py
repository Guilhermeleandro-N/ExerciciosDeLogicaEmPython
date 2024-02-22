#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#        Salário Bruto: (5 * 220)        : R$ 1100,00
#        (-) IR (5%)                     : R$   55,00  
#        (-) INSS ( 10%)                 : R$  110,00
#        FGTS (11%)                      : R$  121,00
#        Total de descontos              : R$  165,00
#        Salário Liquido                 : R$  935,00
valorhora=float(input("Quanto você ganha por horas?"))
horastrabalhadas=float(input("Quantas horas você trabalhou nesse mês?"))
slrbruto=valorhora*horastrabalhadas
if slrbruto<=900:
    ir=float(0)
    irs="0"
elif slrbruto>900 and slrbruto<=1500:
    ir=slrbruto*0.05
    irs=5
elif slrbruto>1500 and slrbruto<=2500:
    ir=slrbruto*0.1
    irs=10
else:
    ir=slrbruto*0.2
    irs=20

inss=slrbruto*0.1
sindicato=slrbruto*0.03
fgts=slrbruto*0.11
slrliquido=slrbruto-sindicato-ir-inss
print(f"""        Salário Bruto: ({valorhora*horastrabalhadas})        
        (-) IR ({irs}%)                    : R$  {ir}  
        (-) INSS ( 10%)                 : R$  {round(inss,2)}
        (-) SINDICATO(3%)               : R$  {round(sindicato,2)}
        FGTS (11%)                      : R$  {round(fgts,2)}
        Total de descontos              : R$  {round((ir+inss+sindicato),2)}
        Salário Liquido                 : R$  {round(slrliquido)}""")


    