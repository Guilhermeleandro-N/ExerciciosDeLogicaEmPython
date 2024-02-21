mb=float(input("Qual o tamanho do arquivo?(Em MB)"))
mbps=float(input("Qual a velocidade de dowload do link?(Mbps)"))
tempo=int(mb/(mbps*60))
print(f"{tempo} minutos restantes...")
