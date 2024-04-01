"""Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:
Código da cidade;
Número de veículos de passeio (em 1999);
Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
Qual a média de veículos nas cinco cidades juntas;
Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio."""
codigo=[]
veiculos=[]
acidentes=[]
somav=0
somaa=0
cont=0
for c in range(5):
    vlr=int(input("Qual o código da cidade?"))
    codigo.append(vlr)
    vlr=int(input("Número de carros a passeios?"))
    veiculos.append(vlr)
    vlr=int(input("Número de acidentes de trãnsito com vitimas:"))
    acidentes.append(vlr)
    somav+=veiculos[c]
    if veiculos[c]<2000:
        cont+=1
        somaa+=acidentes[c]
    if c==0:
        maior=acidentes[c]
        pmaior=c
        menor=acidentes[c]
        pmenor=c
    else:
        if maior<acidentes[c]:
            maior=acidentes[c]
            pmaior=c
        if menor>acidentes[c]:
            menor=acidentes[c]
            pmenor=c
print(f"A cidade com mais acidentes é do código: {codigo[pmaior]} com {acidentes[pmaior]} acidentes .")
print(f"A cidade com menos acidentes é do código: {codigo[pmenor]} com {acidentes[pmenor]} acidentes .\n")
print(f"A média de veículos é {(somav/5):.2f}")
print(f"A media de acidentes em cidades com menos de 2000 veículos é {(somaa/cont):.2f}")


