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
    return memo[n-1][m-1]


def traza():
    n=len(l1)+1
    m=len(l2)+1
    stdout.write(f.'{}\n',memo[n][m])
    int step = 0, i = n, j = m;
    while (i || j) {
        if (x[i - 1] == y[j - 1]) {
            i--, j--;
            continue;
        }
        printf("%d ", ++step);
        if (i > 0 && f[i][j] == f[i - 1][j] + 1) { // delete
            printf("Delete %d", i);
            x.erase(i - 1, 1);
            i--;
        }
        else if (j > 0 && f[i][j] == f[i][j - 1] + 1) { // insert
            printf("Insert %d,%c", i + 1, y[j - 1]);
            x.insert(i, 1, y[j - 1]);
            j--;
        }
        else if (i > 0 && j > 0) {  // replace
            printf("Replace %d,%c", i, y[j - 1]);
            x[i - 1] = y[j - 1];
            i--, j--;
        }
        putchar('\n');
    }
}

memo=[[-1 for _ in range(100)] for _ in range(100)]
for i in range(100): memo[i][0] = i 
for j in range(100): memo[0][j] = j  








while True:
    l1=stdin.readline().strip()
    l2=stdin.readline().strip()
    
    stdout.write(str(edist(l1,l2))+"\n")
    
