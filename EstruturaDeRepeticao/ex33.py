"""O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas."""
n=int(input("Quantas temperaturas você ira informar? "))
soma=0
for c in range(n):
    vlr=float(input("informe uma temperatura: "))
    #soma
    soma+=vlr
    #maior
    if c==0:
        maior=vlr
        menor=vlr
    elif vlr>maior:
        maior=vlr
    #menor
    if c>0 and vlr<menor:
        menor=vlr
media=soma/n
print(f"\nA maior temperatura informada foi: {maior:.2f}°.\nA menor temperatura informada foi: {menor:.2f}°\nA media das temperaturas é {media:.2f}°")