#Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
#   A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#   A mensagem "Reprovado", se a média for menor do que sete;
#   A mensagem "Aprovado com Distinção", se a média for igual a dez.
nota1=float(input("Qual a primeira nota do aluno?\n"))
nota2=float(input("Qual a segunda nota do aluno?\n"))
ntfinal=(nota1+nota2)/2
if ntfinal>=7 and ntfinal!=10:
    print("Aprovado")
elif ntfinal<7:
        print("Reprovado")
elif ntfinal==10:
            print("Aprovado com distinção")
