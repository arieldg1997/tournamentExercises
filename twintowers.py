from sys import stdin, stdout

def lcs(l1,l2):
    n=len(l1)+1
    m=len(l2)+1
    memo = [[0] * m for i in range(n)]
    for I in range(1,n):
        for J in range(1,m):
            if l1[I-1]==l2[J-1]: memo[I][J]=memo[I-1][J-1]+1
            else: memo[I][J]=max(memo[I-1][J],memo[I][J-1])
    return memo[len(l1)][len(l2)]



[a,b] = stdin.readline().strip().split()
sec_num=0
while int(a)!=0 or int(b)!=0:
    sec_num+=1
    stdout.write("Twin Towers #"+str(sec_num)+"\n")
    vector_a=stdin.readline().strip().split()
    vector_b=stdin.readline().strip().split()
    ret=lcs(vector_a,vector_b)
    stdout.write("Number of Tiles : "+str(ret)+"\n")
    stdout.write("\n")
    [a,b] = stdin.readline().strip().split()
