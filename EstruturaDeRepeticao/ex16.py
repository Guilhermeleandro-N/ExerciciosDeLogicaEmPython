"""A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500."""
f=[0,1]
c=2
while True:
    f.append(f[c-1]+f[c-2])
    if f[c]>500:
        break
    c+=1
print(f)