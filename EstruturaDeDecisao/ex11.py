#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.
slratual=float(input("Salario atual:\n"))
if slratual<=280:
    aumento=round((slratual*0.2),2)
    taxa="20%"
elif slratual>280 and slratual<700:
    aumento=round((slratual*0.15),2)
    taxa="15%"
elif slratual>700 and slratual<1500:
    aumento=round((slratual*0.1),2)
    taxa="10%"
elif slratual>1500:
    aumento=round((slratual*0.05),2)
    taxa="5%"

slrnovo=round((slratual+aumento),2)
print(f"O seu salário antigo era: {slratual}\nO percentual de aumento foi:{taxa}\nO valor do aumento foi de {aumento}\nO seu novo salario é {slrnovo}")
