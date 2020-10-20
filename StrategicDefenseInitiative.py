from sys import stdin,stdout



n=int(stdin.readline().strip())
stdin.readline()
for k in range(n):
    if k!=0: stdout.write("\n")
    s=stdin.readline().strip()
    vector=[]
    while s!="":
        vector.append(int(s))
        s=stdin.readline().strip()
    l=[1]*len(vector)
    lprev=[-1]*len(vector)
    ans=0
    for i in range(len(l)):
        for j in range(i):
            if vector[j]<vector[i] and l[i]<l[j]+1:
                l[i]=l[j]+1
                lprev[i]=j
        if l[ans]<l[i]: ans=i

    stdout.write("Max hits: "+str(l[ans])+"\n")
    imp=[]
    while ans!=-1:
        imp.insert(0,vector[ans])
        ans=lprev[ans]
    
    for elem in imp: stdout.write(str(elem)+"\n")
    