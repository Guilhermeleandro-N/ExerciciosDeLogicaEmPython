"""Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . )."""
mes=["1 - Janeiro",  "2 - Fevereiro", "3 - Março", "4 - Abril", "5 - Maio", "6 - Junho", "7 - Julho", "8 - Agosto", "9 - Setembro", "10 - Outubro", "11 - Novembro", "12 - Dezembro"]
soma=0
temp=[]
for c in range(12):
    x=(float(input(f"Qual a temperatura de {(mes[c])[4:]}? ")))
    temp.append(x)
    soma+=x
media=round((soma/12),2)
print(f"A media de temperatura do ano foi: {media} ºC.\nEsses são os meses que ficaram acima da média e suas temperaturas:")
for c in range(12):
    if temp[c]>media:
        print(f"{(mes[c])[4:]} - {temp[c]:.2f} ºC")
