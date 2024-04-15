""""Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:
Maior e Menor Acerto;
Total de Alunos que utilizaram o sistema;
A Média das Notas da Turma.
Gabarito da Prova:

01 - A
02 - B
03 - C
04 - D
05 - E
06 - E
07 - D
08 - C
09 - B
10 - A
Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova antes dos alunos usarem o programa."""
gabarito=["A","B","C","D","E","E","D","C","B","A"]
cont=0
notas=[]
soma=0
#prenche o gabarito do aluno
while True:
    cont+=1
    resposta=[]
    nota=0
   
    print("Insira o gabarito do Aluno:")
    for c in range(1,11):
        p=input(f"{c} questão: ")
        p=p.upper()
        resposta.append(p)
    for c in range(10):
        if (gabarito[c]==resposta[c]):
            nota+=1
    
    soma+=nota
    notas.append(nota)
    while True:
        r=input("Deseja colocar a nota de outro aluno?[S/N] ")
        r=r.upper()
        if r=="N":
            break     
        elif r=="S":
            break
        else:
            print("Resposta inválida, responda novamente!")

    if r=="N":
        break
notas.sort()
print(f"""
    Maior Acerto:                               {notas[cont-1]}
    Menor acerto:                               {notas[0]}
    Total de Alunos que utilizaram o sistema:   {cont}
    A Média das Notas da Turma:                 {(soma/cont):.2f}""")

        
        
