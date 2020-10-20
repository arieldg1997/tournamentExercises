from sys import stdin,stdout


def lcs(l1,l2):
    n=len(l1)+1
    m=len(l2)+1
    memo = [[0] * m for i in range(n)]
    for I in range(1,n):
        for J in range(1,m):
            if l1[I-1]==l2[J-1]: memo[I][J]=memo[I-1][J-1]+1
            else: memo[I][J]=max(memo[I-1][J],memo[I][J-1])
    return memo[len(l1)][len(l2)]
    


case_number=1

for line in stdin:
    line1=line
    if line1[0]=="#": break
    line2=stdin.readline()
    ret=lcs(line1,line2)-1
    stdout.write("Case #"+str(case_number)+": you can visit at most "+str(ret)+" cities.\n")
    case_number+=1
