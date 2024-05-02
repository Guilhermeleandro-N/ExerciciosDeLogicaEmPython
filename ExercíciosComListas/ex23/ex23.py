"""A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos. Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":
alexandre       456123789
anderson        1245698456
antonio         123456456
carlos          91257581
cesar           987458
rosemary        789456125
Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa que gere um relatório, chamado "relatório.txt", no seguinte formato:
ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso

1    alexandre       434,99 MB             16,85%
2    anderson       1187,99 MB             46,02%
3    antonio         117,73 MB              4,56%
4    carlos           87,03 MB              3,37%
5    cesar             0,94 MB              0,04%
6    rosemary        752,88 MB             29,16%

Espaço total ocupado: 2581,57 MB
Espaço médio ocupado: 430,26 MB
O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários, de forma a agilizar a execução do programa. A conversão da espaço ocupado em disco, de bytes para megabytes deverá ser feita através de uma função separada, que será chamada pelo programa principal. O cálculo do percentual de uso também deverá ser feito através de uma função, que será chamada pelo programa principal."""
#definição das funções
def byte_para_mega(byte):
    return (byte/1048576 )
def porcentagem(mb,soma):
    return (mb/soma)*100
#declaração de variáveis
usuarios=[]
bytes=[]
mb=[]
porcento=[]
soma=0
#abre o arquivo .txt
texto=open("usuarios.txt","rt")
linha=texto.readlines()
#prenche a lista usuarios e bytes
for c in linha:
    x=c[:16]
    y=int(c[16:])
    usuarios.append(x)
    bytes.append(y)
#prenche a lista mb e soma o total
for c in range(len(bytes)):
    x=byte_para_mega(bytes[c])
    mb.append(round(x,2))
    soma+=mb[c]
#calcula a porcentagem
for c in range(len(mb)):
    x=porcentagem(mb[c],soma)
    porcento.append(round(x,2))
#impreção dos resultados
print("""------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso
""")
for c in range(len(linha)):
    print(f"{c+1}    {usuarios[c]}{mb[c]} MB             {porcento[c]}%")
print(f"""Espaço total ocupado: {round(soma,2)} MB
Espaço médio ocupado: {round(soma/len(linha),2)} MB""")
input()





    