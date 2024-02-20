
tmhtotal=(float(input("Quantos metros quadrados precisam ser pintados?\n")))
tmhtotal=tmhtotal*1.1
divint=0
divint=tmhtotal//108
divmod=tmhtotal%108
divintg=0
if divmod != 0 or divint==0:   
    divintg=divmod//21.6    
    divmodg=divmod%21.6
    if divmodg != 0:
        divintg+=1
        

print(f"Você vai precisar de {divint} balde(s) de tinta(s) e de {divintg} galões de tinta que custam {round(((divint*80)+divintg*25),2)} R$.")