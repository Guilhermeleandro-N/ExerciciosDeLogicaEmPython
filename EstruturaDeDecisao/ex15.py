#Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
#Dicas:
#Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#Triângulo Equilátero: três lados iguais;
#Triângulo Isósceles: quaisquer dois lados iguais;
#Triângulo Escaleno: três lados diferentes;
print("Me informe o comprimento em CM dos três lados da forma geometrica:")
a=float(input("Lado a:\n"))
b=float(input("Lado b:\n"))
c=float(input("lado c:\n"))
##Alocar a hipotenusa na variavel "a"
if (b>=a) and (b>=c):
    aux=a
    a=b
    b=aux
elif (c>=a) and (c>=b):
    aux=a
    a=c
    c=aux

##Definir o tipo de triangulo
print(f"lado a={a}\n")
print(f"lado b={b}\n")
print(f"lado ac={c}\n")
if a<(b+c):
    if (a==b) and (a==c):
        print("Triangulo equilátero!")
    elif (a==b) or (b==c) or (c==a):
        print("Triangulo Isóceles!")
    elif a!=b and a!=c and b!=c:
        print("Triangulo Escaleno!")
else:
    print("Não forma um triangulo!")