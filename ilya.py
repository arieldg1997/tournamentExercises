from sys import stdin,stdout


vector=stdin.readline().strip()
aux_vector=[-1]*len(vector)
cases=int(stdin.readline().strip())
tope=0
aux_vector[0]=0
for i in range(cases):
    par=stdin.readline().strip().split()
    a=int(par[0])-1
    b=int(par[1])-1
    if aux_vector[b]==-1:
        cont=aux_vector[tope]
        for j in range(tope, b):
            if vector[j]==vector[j+1]: cont+=1
            aux_vector[j+1]=cont
        tope=b
    stdout.write(str(aux_vector[b]-aux_vector[a])+'\n')