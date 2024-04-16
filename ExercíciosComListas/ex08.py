"""Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida."""
lista=[[],[],[],[],[]]

for c in range(5):
        idade=int(input(f"Qual a idade da {c+1}ª pessoa?"))
        altura=float(input(f"Qual a altura da {c+1}ª pessoa?"))
        lista[c].append(idade)
        lista[c].append(altura)
for c in range(4,-1,-1):
        print(f"A idade e altura da {c+1}ª pessoa:{lista[c]}")
        
        
