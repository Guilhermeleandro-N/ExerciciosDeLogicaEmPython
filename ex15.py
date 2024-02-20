##quanto ganha por hora
#numero de horas trabalhadas no mes 
#-11% imposto de renda
#-8% para inss
#-5% para sidicato
porhora=float(input("Quanto você ganha por hora?"))
horas=float(input("Quantas horas você trabalhou?"))
salariobruto=porhora*horas
renda=salariobruto*0.11
inss=salariobruto*0.08
sindicato=salariobruto*0.05
salarioliquido=salariobruto-renda-inss-sindicato
print(f"Seu salário bruto é {round(salariobruto,2)}.\nSeu desconto do imposto de renda foi {round(renda,2)}\nDesconto INSS foi {round(inss,2)}\nO desconto do sindicato foi {round(sindicato,2)}\nSeu salario líquido é {round(salarioliquido,2)}")