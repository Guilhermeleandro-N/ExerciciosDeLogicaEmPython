#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
data=input("Escreva uma data no formato dd/mm/aaaa:")
datasplit=data.split("/")
dia=int(datasplit[0])
mes=int(datasplit[1])
ano=int(datasplit[2])
if(dia>0 and dia<31) and (mes>0 and mes<13) and (ano>999):
    print("A data abaixo é válida")
else:
    print("A data abaixo não é válida")
print(f"Dia:{datasplit[0]}\nMês:{datasplit[1]}\nAno:{datasplit[2]}")
