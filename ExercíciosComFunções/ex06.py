"""Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar."""
#modifiquei para a maneira em que achei mais interessante
def conversao(horario):
    horas=horario.split(":")
    horas[0]=int(horas[0])
    horas[1]=int(horas[1])
    if horas[0]>=12:
        horas[0]-=12
        horas.append("P.M")
    else:
        horas.append("A.M")
    return horas
def impressao(horas):
    print(f"{str(horas[0]).zfill(2)}:{str(horas[1]).zfill(2)} {horas[2]}")

while True:
    while True:
        horario=input("Me informe um horario em notação de 24 horas no formato hh:mm(ex: 14:25) que converterei para o formato A.M/P.M.\nHorário: ")
        if (":" in horario):
            break
        else:
            print("A horário não está no formato especificado.")    
    impressao(conversao(horario))
    r=input("Deseja realizar outra conversão?[S/N]").upper()
    if r=="N":
        break
print("Programa finalizado!")
