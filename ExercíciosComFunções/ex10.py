"""Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, obtendo um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". Seu objetivo agora é continuar jogando os dados até tirar este número novamente. Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente."""
import random
def primeira(x):
    if x in [7,11]:
        return "Você venceu!"
    elif x in [2,3,12]:
        return "Crap! Você perdeu!"
    elif x in [4,5,6,8,9,10]:
        return x
cont=0
def outras_jogadas(x,z):
        if x==7:
            print("Você perdeu!")
            return True
        elif z==x:
            print("Você venceu!")
            return True

while True:
    x=random.randint(2,12)    
    print(f"O valor dos dados foi {x}")
    if cont==0:  
        z=primeira(x)  
        if isinstance(z,str):         
            print(z)
            break    
    else:
        if outras_jogadas(x,z):
            break
    cont+=1
