"""A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo."""
vezes=int(input("Quantas termos da série fibonacci você deseja ver?"))
f=[0,1]
for c in range(2,vezes):
    f.append(f[c-1]+f[c-2])
print(f)

