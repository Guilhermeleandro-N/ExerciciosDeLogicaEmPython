"""Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber qual o melhor jogador após cada jogo. Para isto, faz-se necessário o desenvolvimento de um programa, que será utilizado pelas telefonistas, para a computação dos votos. Sua equipe foi contratada para desenvolver este programa, utilizando a linguagem de programação C++. Para computar cada voto, a telefonista digitará um número, entre 1 e 23, correspondente ao número da camisa do jogador. Um número de jogador igual zero, indica que a votação foi encerrada. Se um número inválido for digitado, o programa deve ignorá-lo, mostrando uma breve mensagem de aviso, e voltando a pedir outro número. Após o final da votação, o programa deverá exibir:
O total de votos computados;
Os númeos e respectivos votos de todos os jogadores que receberam votos;
O percentual de votos de cada um destes jogadores;
O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos e o percentual de votos dados a ele.
Observe que os votos inválidos e o zero final não devem ser computados como votos. O resultado aparece ordenado pelo número do jogador. O programa deve fazer uso de arrays. O programa deverá executar o cálculo do percentual de cada jogador através de uma função. Esta função receberá dois parâmetros: o número de votos de um jogador e o total de votos. A função calculará o percentual e retornará o valor calculado. Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa. Ao final, o programa deve ainda gravar os dados referentes ao resultado da votação em um arquivo texto no disco, obedecendo a mesma disposição apresentada na tela.
Enquete: Quem foi o melhor jogador?

Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 11
Número do jogador (0=fim): 10
Número do jogador (0=fim): 50
Informe um valor entre 1 e 23 ou 0 para sair!
Número do jogador (0=fim): 9
Número do jogador (0=fim): 9
Número do jogador (0=fim): 0

Resultado da votação:

Foram computados 8 votos.

Jogador Votos           %
9               4               50,0%
10              3               37,5%
11              1               12,5%
O melhor jogador foi o número 9, com 4 votos, correspondendo a 50% do total de votos."""
#declaração de variáveis
def porcento(total, njogador):
    porcentagem=round(((njogador/total)*100),2)
    return porcentagem
contadores=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
porcentagem=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
votos=0
indice=0
#votação
while True:
    x=int(input("Número do jogador: (0=fim) "))
    if x>0 and x<24:
        contadores[x-1]+=1
        votos+=1
    elif x==0:
        break
    else:
        print("Informe um valor entre 1 e 23 ou 0 pra sair!")
#resultado da votação
print("Resultado da votação: \nJogador              votos              %")
maior=contadores[0]
for c in range(23):
    if contadores[c]>maior:
        maior=contadores[c]
        indice=c
    if contadores[c]>0:
        porcentagem[c]=porcento(votos, contadores[c])
        print(f"{c+1}                {contadores[c]}             {porcentagem[c]}")
        
print(f"O melhor jogador foi o número {indice+1}, com {contadores[indice]} votos, correspondendo a {porcentagem[indice]}% do total de votos.")
    
#escrita no arquivo.txt
with open("texto.txt", "w") as texto:
    texto.write("Resultado da votação: \nJogador              votos              %\n")
    for c in range(23):
        if contadores[c]>0:
            texto.write(f"{c+1}                {contadores[c]}             {porcentagem[c]}\n")
    texto.write(f"O melhor jogador foi o número {indice+1}, com {contadores[indice]} votos, correspondendo a {porcentagem[indice]}% do total de votos.")
input("Pressione enter para sair...")