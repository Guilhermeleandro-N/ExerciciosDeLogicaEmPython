"""Embaralha palavra. Construa uma função que receba uma string como parâmetro e devolva outra string com os carateres embaralhados. Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinação possível, de forma aleatória. Padronize em sua função que todos os caracteres serão devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados."""
import random
def embaralha_palavra(palavra):
    novapalavra=[]
    for c in range(len(palavra)):
        novapalavra.append(palavra[c])
        lista=[]
    for c in range(len(palavra)):      
        while True:
            x=random.randint(0,len(palavra)-1)
            if not(x in lista):
                novapalavra[c]=palavra[x] 
                lista.append(x)
                break
    novapalavra=''.join(novapalavra)
    if 0==(random.randint(0,1)):
        novapalavra=novapalavra.upper()
    else:
        novapalavra=novapalavra.lower()

    return novapalavra
    
palavra=input("M e informe uma palavra: ")
embaralhada=embaralha_palavra(palavra)
for c in embaralhada:
    print(c, end="")