from sys import stdin,stdout

elephants=[]
n=0
for line in stdin:
    line=line.strip().split()
    n+=1
    elephants.append((int(line[0]),int(line[1]),n))
elephants.sort(key=lambda x: x[0])



l=[-1]*len(elephants)
lprev=[-1]*len(elephants)
def lis(vector, idx):
    global l,lprev
    if (l[idx]!=-1): return l[idx]
    l[idx]=1
    for i in range(0,idx):
        if ((vector[i][1] > vector[idx][1]) and l[idx] < lis(vector,i) + 1):
            l[idx] = lis(vector,i) + 1
            lprev[idx] = i

    return l[idx]

max_actual=-1
for i in reversed(range(len(elephants))):
    j=lis(elephants,i)
    if max_actual<j: max_actual=j

ok=True
array=[]
indice=l.index(max_actual)
while ok:
    array.insert(0,elephants[indice][2])
    indice=lprev[indice]
    if indice==-1: ok=False

stdout.write(str(len(array))+"\n")
for n in array:
    stdout.write(str(n)+"\n")







