from sys import stdin,stdout

cases=int(stdin.readline().strip())
for c in range(cases):
    cant=0
    pila=[]
    array=stdin.readline().strip()
    for i in range(len(array)):
        if array[i]=='<':
            pila.append('<')
        if array[i]=='>':
            if pila:
                cant+=1
                pila.pop(0)
    stdout.write(str(cant)+'\n')              
