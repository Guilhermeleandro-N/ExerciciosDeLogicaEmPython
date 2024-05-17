#Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida.
def data_extenso(data):
    meses = ["Janeiro", "Fevereiro", "Março", "Abril","Maio", "Junho", "Julho", "Agosto","Setembro", "Outubro", "Novembro", "Dezembro"]
    lista=data.split("/")
    cont=0
    for c in lista:
     lista[cont]=int(lista[cont])
     cont+=1
    if len(lista)==3:
        if (lista[0]>0 and lista[0]<31) and (lista[1]>0 and lista[1]<=12) and (lista[2]>0 and lista[2]<=3000):
            return f"{str(lista[0]).zfill(2)} de {meses[lista[1]-1]} de {lista[2]}!"
        else:
           return 0
    else:
        return 0

while True:
    data=input("Me informe uma data no formata DD/MM/AAAA.")
    if "/" in data:
        x=data_extenso(data)
        if isinstance(x,str):
           print(x)
           break
        else:
           print("A data informada não está no formato pedido!")
    else:
       print("A data informada não esta no formato pedido!")
       

    