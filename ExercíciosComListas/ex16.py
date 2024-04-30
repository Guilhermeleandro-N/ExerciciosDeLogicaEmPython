"""Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
$200 - $299
$300 - $399
$400 - $499
$500 - $599
$600 - $699
$700 - $799
$800 - $899
$900 - $999
$1000 em diante
Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados."""
contadores=[0,0,0,0,0,0,0,0,0]
x=int(input("De quantos funcionários você irá informar o salário?"))
salarios=[]
for c in range(x):
    salario=float(input(f"Salario do {c+1} funcionário: "))
    salarios.append(salario)
    
    indice=int((salarios[c]-200)//100)
    if indice<8:
        contadores[indice]+=1
    else:
        contadores[8]+=1
print(f"""O numero de funcinários recebendo...
      $200 a $299: {contadores[0]}
      $300 a $399: {contadores[1]}
      $400 a $499: {contadores[2]}
      $500 a $599: {contadores[3]}
      $600 a $699: {contadores[4]}
      $700 a $799: {contadores[5]}
      $800 - $899: {contadores[6]}
      $900 - $999: {contadores[7]} 
      $1000 em diante {contadores[8]}""")
