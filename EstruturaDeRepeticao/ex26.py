"""Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato."""
n=int(input("Quantos eleitores participarão nessa eleição?\n"))
afonso=0
bianca=0
cesar=0
for c in range(n):
    voto=input("Afonso  //Bianca  //César   \nVote [A] //Vote [B] //Vote [C] \n").upper()
    if voto=="A":
        afonso+=1
    elif voto=="B":
        bianca+=1
    elif voto=="C":
        cesar+=1
print(f"\t\t  RESULTADOS\nAfonso  //Bianca  //César   \n [{afonso}] //\t [{bianca}] \t //[{cesar}] ")
