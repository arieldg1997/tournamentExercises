from sys import stdin, stdout

def edist(l1,l2): 
    n=len(l1)+1
    m=len(l2)+1
    for i in range(1,n):
        for j in range(1,m):
            replace=memo[i-1][j-1] + int(l1[i-1]!=l2[j-1])
            delete=memo[i-1][j] + 1
            insert=memo[i][j-1] + 1 
            memo[i][j] = min(replace,delete,insert) 
    traza(n-1,m-1,l1,l2)
    return memo[n-1][m-1]


def traza(i,j,l1,l2):
    while i>0 or j>0:
        if i>0 and j>0 and l1[i-1] == l2[j-1]:
            i-=1
            j-=1
        elif i>0 and memo[i][j] == memo[i-1][j] +1:
            operations.insert(0,("Delete",i,"\n"))
            i-=1
        elif j>0 and memo[i][j] == memo[i][j-1] +1:
            operations.insert(0,("Insert",i+1,","+l2[j-1]+"\n"))
            j-=1
        elif i>0 and j>0 and l1[i-1] != l2[j-1]:
            operations.insert(0,("Replace",i,","+l2[j-1]+"\n"))
            i-=1
            j-=1

memo=[[-1 for _ in range(100)] for _ in range(100)]
for i in range(100): memo[i][0] = i 
for j in range(100): memo[0][j] = j  

buliano=True
for line in stdin:
    l1=line.strip()
    l2=stdin.readline().strip()
    if buliano==False: stdout.write("\n")
    else: buliano=False
    operations=[]
    n=edist(l1,l2)
    stdout.write(str(n)+"\n")
    sesgo=0
    for elem in range(n):
        aux=operations[elem]
        stdout.write(str(elem+1)+" "+aux[0]+" "+str(aux[1]+sesgo)+aux[2])
        if operations[elem][0]=="Delete": sesgo-=1
        elif operations[elem][0]=="Insert": sesgo+=1