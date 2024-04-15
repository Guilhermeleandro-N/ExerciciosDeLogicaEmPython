"""O cardápio de uma lanchonete é o seguinte:
Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00
Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado."""
#Decidi fazer um caixa, durante o programa entra o input do codigo do produto e posteriomanete o valor pago. No fim, é gerado uma nota fiscal.
soma=0
b100=0
b101=0
b102=0
b103=0
b104=0
b105 = 0
lista=[]
#Computa a quantidade de itens, valor de pedido por item e total(soma)
print(f"""Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00\n""")
while True:
    cod=int(input("Código: "))
    if cod==100:
        b100+=1
        soma+=1.2 
    elif cod==101:
        b101+=1
        soma+=1.3
    elif cod==102:
        b102+=1
        soma+=1.5
    elif cod==103:
        b103+=1
        soma+=1.2     
    elif cod==104:
        b104+=1
        soma+=1.3     
    elif cod==105:
        b105+=1
        soma+=1    
    if cod<100 or cod>105:
        break

pago=float(input(f"O total foi {soma:.2f}\nValor pago pelo cliente: "))
print(f"\n\n")
troco=pago-soma
#Cria a string do nome do produto, valor unitario , quantidade e valor total 
print(f"Produto                                                  valor           ")
if b100>0:
    lista.append((f"""Cachorro quente     
                                R$1,20*{b100} uni\t\t R${(1.2*b100):.2f}"""))
if b101>0:
    lista.append((f"""Bauru Simples       
                                R$1,30*{b101} uni\t\t R${(1.3*b101):.2f}"""))
if b102>0:
    lista.append((f"""Bauru com ovo       
                                R$1,50*{b102} uni\t\t R${(1.5*b102):.2f}"""))
if b103>0:
    lista.append((f"""Hambúrguer          
                                R$1,20*{b103} uni\t\t R${(1.2*b103):.2f}"""))
if b104>0:
    lista.append((f"""Cheeseburguer       
                                R$1,30*{b104} uni\t\t RS{(1.3*b104):.2f}"""))
if b104>0:
    lista.append((f"""Refrigerante        
                                R$1,00*{b105} uni\t\t R${(1*b105):.2f}"""))
for c in lista:
    print(c)
print()
print(            f"Valor recebido                                           R${pago:.2f}")
print(            f"Troco                                                    R${troco:.2f}")
print(            f"Total                                                    R${soma:.2f}")

input()
    
    
    


