"""Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:
1 , 2, 3, 4  - Votos para os respectivos candidatos 
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco
Faça um programa que calcule e mostre:
O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;
A percentagem de votos nulos sobre o total de votos;
A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.
"""
jose=0
joao=0
jamires=0
jucilania=0
nulo=0
branco=0
print("""Votação!
      João - 1
      José - 2
      Jamires - 3
      Jucilania - 4
      Nulo - 5
      Branco - 6
      0 encerra a votação!""")

while True:
    x=int(input("Qual seu voto? "))
    if x==0:
        break
    elif x==1:
        jose+=1
    elif x==2:
        joao+=1
    elif x==3:
        jamires+=1
    elif x==4:
        jucilania+=1
    elif x==5:
        nulo+=1
    elif x==6:
        branco+=1

total=joao+jose+jamires+jucilania+nulo+branco
print(f"""Resultado!
      joão - {joao} votos
      José - {jose} votos
      Jamires - {jamires} votos
      Jucilania - {jucilania} votos
      Nulo - {nulo} votos
      Branco - {branco} votos
      {((nulo/total)*100):.2f}% de votos nulos
      {((branco/total)*100):.2f}% de votos em branco""")


