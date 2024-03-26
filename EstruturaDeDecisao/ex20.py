"""Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
A mensagem "Aprovado com Distinção", se a média for igual a 10."""
n1=float(input("Qual a primeira nota do aluno?\n"))
n2=float(input("Qual a segunda nota do aluno?\n"))
n3=float(input("Qual a terceira nota do aluno?\n"))
media=round(((n1+n2+n3)/3),2)
print(f"Média: {media}")
if (media==10):
    print("Aprovado com distinção")
elif (media>=7):
    print("Aprovado")
elif (media<7):
    print("Reprovado")


