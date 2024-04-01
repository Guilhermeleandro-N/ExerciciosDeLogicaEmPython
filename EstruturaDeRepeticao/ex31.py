"""O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:
Lojas Tabajara 
Produto 1: R$ 2.20
Produto 2: R$ 5.80
Produto 3: R$ 0
Total: R$ 9.00
Dinheiro: R$ 20.00
Troco: R$ 11.00
..."""
while True:
    valores=[]
    cont=0
    soma=0
    print("//\t\tCaixa registradora inciada")
    while True:
        valor=float(input("Valor do produto: "))
        valores.append(valor)
        cont+=1
        if valor==0:
            break
    for c in range(1,cont+1):
        print(f"Produto {c}: R$ {valores[c-1]:.2f}")
        soma+=valores[c-1]
    print(f"\nTotal: R$ {soma:.2f}")
    recebido=float(input("Valor recebido do cliente: "))
    print(f"Troco: R$ {(recebido-soma):.2f}")
    while True:
        R=input("Continuar o programa?[S/N] ").upper()
        if R=="S" or R=="N":
            break
        else:
            print("Informe uma resposta válida!")
    if R=="N":
        break
    
