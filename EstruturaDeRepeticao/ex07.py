"Faça um programa que leia 5 números e informe o maior número."
for x in range(1,6):
   a=float(input("Digite um valor:"))
   if x==1:
      maior=a
   elif a>maior:
      maior=a
print(f"//\tO maior numero informado foi {maior}.")
