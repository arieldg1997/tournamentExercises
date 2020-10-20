from sys import stdin,stdout

#Solucion cuadratica 180ms
n=int(stdin.readline().strip())
vector=stdin.readline().strip().split()
for i in range(len(vector)):
    vector[i]=int(vector[i])
l=[1]*n
lprev=[-1]*n
ans=0
for i in range(len(l)):
    for j in range(i):
        if vector[j]<vector[i] and l[i]<l[j]+1:
            l[i]=l[j]+1
            lprev[i]=j
    if l[ans]<l[i]: ans=i

stdout.write(str(l[ans]))
