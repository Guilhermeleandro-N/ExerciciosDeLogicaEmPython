"""Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer um levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar todos os cerca de 200 mouses que se encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles.
Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá receber um número indeterminado de entradas, cada uma contendo: um número de identificação do mouse o tipo de defeito:
necessita da esfera;
necessita de limpeza; a.necessita troca do cabo ou conector; a.quebrado ou inutilizado Uma identificação igual a zero encerra o programa. Ao final o programa deverá emitir o seguinte relatório:
Quantidade de mouses: 100

Situação                        Quantidade              Percentual
1- necessita da esfera                  40                     40%
2- necessita de limpeza                 30                     30%
3- necessita troca do cabo ou conector  15                     15%
4- quebrado ou inutilizado              15                     15%"""
contadores=[0,0,0,0,0]
ident=[]
porcentagens=[]
print("""Problemas possíveis:
      1- necessita da esfera 
      2- necessita de limpeza
      3- necessita troca do cabo ou conector
      4- quebrado ou inutilizado """)
while True:
    x=int(input("Número de identificação do Mouse:"))
    y=int(input("Qual o problema apresentado? [1/2/3/4/0=Fim]"))
    if y==0:
        break
    elif y<0 or y>4:
        print("Opção inválida!")
        continue
    ident.append(x)
    contadores[y]+=1
    contadores[0]+=1
for c in range(0,5):
    z=round((contadores[c]/contadores[0]*100),2)
    porcentagens.append(z)


print(f"""Quantidade de mouses: {contadores[0]}
      
    Situação                        Quantidade              Percentual
    1- necessita da esfera                  {contadores[1]}                     {porcentagens[1]}%
    2- necessita de limpeza                 {contadores[2]}                     {porcentagens[2]}%
    3- necessita troca do cabo ou conector  {contadores[3]}                     {porcentagens[3]}%
    4- quebrado ou inutilizado              {contadores[4]}                     {porcentagens[4]}%""")