"""As Organizações Tabajara resolveram dar um abono aos seus colaboradores em reconhecimento ao bom resultado alcançado durante o ano que passou. Para isto contratou você para desenvolver a aplicação que servirá como uma projeção de quanto será gasto com o pagamento deste abono.
Após reuniões envolvendo a diretoria executiva, a diretoria financeira e os representantes do sindicato laboral, chegou-se a seguinte forma de cálculo:
a.Cada funcionário receberá o equivalente a 20% do seu salário bruto de dezembro; a.O piso do abono será de 100 reais, isto é, aqueles funcionários cujo salário for muito baixo, recebem este valor mínimo; Neste momento, não se deve ter nenhuma preocupação com colaboradores com tempo menor de casa, descontos, impostos ou outras particularidades. Seu programa deverá permitir a digitação do salário de um número indefinido (desconhecido) de salários. Um valor de salário igual a 0 (zero) encerra a digitação. Após a entrada de todos os dados o programa deverá calcular o valor do abono concedido a cada colaborador, de acordo com a regra definida acima. Ao final, o programa deverá apresentar:
O salário de cada funcionário, juntamente com o valor do abono;
O número total de funcionário processados;
O valor total a ser gasto com o pagamento do abono;
O número de funcionário que receberá o valor mínimo de 100 reais;
O maior valor pago como abono; A tela abaixo é um exemplo de execução do programa, apenas para fins ilustrativos. Os valores podem mudar a cada execução do programa.
Projeção de Gastos com Abono
============================ 
 
Salário: 1000
Salário: 300
Salário: 500
Salário: 100
Salário: 4500
Salário: 0
 
Salário    - Abono     
R$ 1000.00 - R$  200.00
R$  300.00 - R$  100.00
R$  500.00 - R$  100.00
R$  100.00 - R$  100.00
R$ 4500.00 - R$  900.00
 
Foram processados 5 colaboradores
Total gasto com abonos: R$ 1400.00
Valor mínimo pago a 3 colaboradores
Maior valor de abono pago: R$ 900.00
"""
#Declaração de variáveis
salario=[]
cont=0
abono=[]
soma=0
abonomin=0
maior=0
#Prenchimento das variaveis
print("Informe o valor do salário dos funcionário: (Valor 0 = Fim)")
while True:
    aux=float(input("Valor do salário: "))
    if aux==0:
        break
    salario.append(round(aux,2))
    cont+=1
    if aux<=500:
        x=100
        abono.append(x)
        abonomin+=1
    else:
        x=round((aux*0.2),2)
        abono.append(x) 
    soma+=x 
    if maior<x:
        maior=x

#Resultados
print("Salário    - Abono     ")
for c in range(len(salario)):
    print(f"R$ {salario[c]} - R$  {abono[c]}")
print(f"""Foram processados {cont} colaboradores
Total gasto com abonos: R$ {round(soma,2)}
Valor mínimo pago a {abonomin} colaboradores
Maior valor de abono pago: R$ {maior}""")