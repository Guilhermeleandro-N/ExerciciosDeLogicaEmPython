import random
def dado():
    return random.randint(1,6)
contadores=[0,0,0,0,0,0]
lancamento=[]
for c in range(100):
    lancamento.append(dado())
    contadores[lancamento[c]-1]+=1
print("Quantidade de vezes que cada lado caiu:")
for c in range(6):
    print(f"Lado {c+1}:             {contadores[c]}")