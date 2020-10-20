from sys import stdin, stdout, setrecursionlimit

n = int(stdin.readline())
setrecursionlimit(200000)
heights = stdin.readline().strip().split()
#heights=[int(height) for height in heights]
heights = list(map(int, heights))

valores=[-1]*n

def calculo(i):
    if valores[i]!=-1: return valores[i]
    if i==0: return 0
    aux=1
    min_cost=99999999999
    while i-aux>=0:
        dif=abs(heights[i]-heights[i-aux])+calculo(i-aux)
        if min_cost>dif: min_cost=dif
        aux=aux*2  
    valores[i]=min_cost
    return min_cost

ret=calculo(n-1)
stdout.write(str(ret)+'\n')
