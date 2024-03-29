"""Altere o programa anterior para que ele aceite apenas números entre 0 e 1000."""
lista = []
while True:
    n=int(input("Quantos números você ira informar?"))
    if n>=0 and n<=1000:
        break
    else:
        print("Informe um valor entre 0 e 1000.")
for c in range(n):
    a=float(input("Informe um número:"))
    lista.append(a)
for c in range(n):
    if c==0:
        maior=lista[0]
    elif lista[c]>lista[c-1]:
        maior=lista[c]
print(f"O maior número informado foi {maior}.")
for c in range(n):
    if c==0:
        menor=lista[0]
    elif lista[c]<lista[c-1]:
        menor=lista[c]
print(f"O menor número informado foi {menor}.")
soma=0
for c in range(n):
    soma+=lista[c]
print(f"A soma dos números informados é {soma}")
