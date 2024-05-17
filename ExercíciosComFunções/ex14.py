import itertools
def allsquares():
    quadrados = itertools.permutations([1,2,3,4,5,6,7,8,9])
    quadrados=list(quadrados)
    return(quadrados)

def perfectsquare(quadrados):
    quadradosperfeito=[]
    for c in range(len(quadrados)):
        cont=0
        if quadrados[c][0]+quadrados[c][3]+quadrados[c][6]==15:
            cont+=1
        if quadrados[c][1]+quadrados[c][4]+quadrados[c][7]==15:
            cont+=1
        if quadrados[c][2]+quadrados[c][5]+quadrados[c][8]==15:
            cont+=1
        if quadrados[c][0]+quadrados[c][1]+quadrados[c][2]==15:
            cont+=1
        if quadrados[c][3]+quadrados[c][4]+quadrados[c][5]==15:
            cont+=1
        if quadrados[c][6]+quadrados[c][7]+quadrados[c][8]==15:
            cont+=1
        if quadrados[c][0]+quadrados[c][4]+quadrados[c][8]==15:
            cont+=1
        if quadrados[c][2]+quadrados[c][4]+quadrados[c][6]==15:
            cont+=1
        if cont==8:
            quadradosperfeito.append(quadrados[c])
    return quadradosperfeito

quadrados=allsquares()
quadradosperfeito=(perfectsquare(quadrados))
contador=0
for x in range(len(quadradosperfeito)):
    for c in quadradosperfeito[x]:
        contador+=1
        print(f"{c} ", end="")
        if contador%9==0:
            print("\n\n")
        elif contador%3==0:
            print("\n")


