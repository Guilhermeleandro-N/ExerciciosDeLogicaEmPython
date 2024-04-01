"""Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes"""
codigo=[]
peso=[]
altura=[]
cont=0
somaal=0
somape=0
while True:
    vlr=int(input("Código: "))
    if vlr !=0:
        codigo.append(vlr)
    else:
        break
    aux=int(input("Peso: "))
    peso.append(aux)
    aux=int(input("Altura: "))
    altura.append(aux)
    cont+=1
for c in range(cont):
    somaal+=altura[c]
    somape+=peso[c]
    if c==0:
        magro=peso[c]
        gordo=peso[c]
        alto=altura[c]
        baixo=altura[c]
        pbaixo=c
        palto=c
        pmagro=c
        pgordo=c
    else:
        if magro>peso[c]:
            magro=peso[c]
            pmagro=c
        if gordo<peso[c]:
            gordo=peso[c]
            pgordo=c
        if alto<altura[c]:
            alto=altura[c]
            palto=c
        if baixo>altura[c]:
            baixo=altura[c]
            pbaixo=c
mediapeso=somape/cont
mediaaltura=somaal/cont
print(f"\tALUNO MAIS ALTO\nCodigo: {codigo[palto]}\nAltura: {altura[palto]}")
print(f"\tALUNO MAIS BAIXO\nCodigo {codigo[pbaixo]}\nAltura: {altura[pbaixo]}")
print(f"\tALUNO MAIS PESADO\nCódigo: {codigo[pgordo]}\nPeso: {peso[pgordo]}")
print(f"\t ALUNO MAIS LEVE\nCódigo: {codigo[pmagro]}\nPeso: {peso[pmagro]}")


    
