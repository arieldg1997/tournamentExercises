from sys import stdin, stdout

cost_insert=1
cost_delete=1
cost_replace=1


def edist(l1,l2): 
    n=len(l1)+1
    m=len(l2)+1
    for i in range(1,n):
        for j in range(1,m):
            if l1[i-1]!=l2[j-1]: aux=cost_replace
            else: aux=0
            memo[i][j] = memo[i-1][j-1] + aux
            memo[i][j] = min(memo[i][j], memo[i-1][j] + cost_delete)
            memo[i][j] = min(memo[i][j], memo[i][j-1] + cost_insert)
    return memo[n-1][m-1]

 
memo=[[-1 for _ in range(2050)] for _ in range(2050)]
for i in range(2050): memo[i][0] = i * cost_delete
for j in range(2050): memo[0][j] = j * cost_insert 
test_cases=int(stdin.readline().strip())


for case in range(test_cases):
    l1=stdin.readline().strip()
    l2=stdin.readline().strip()
    stdout.write(str(edist(l1,l2))+"\n")