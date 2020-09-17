from sys import stdin, stdout

set=set()
for line in stdin:
    sequence=[]
    jolly=True
    set.clear()
    line=line.strip().split()
    dim=int(line[0])-1
    for I in range(dim):
        dif=abs(int(line[I+2])-int(line[I+1]))
        if 0<dif<=dim:
            set.add(dif)
        else:
            jolly=False
            break
    if len(set)!=dim: jolly=False
    if jolly: stdout.write('Jolly\n') 
    else: stdout.write('Not jolly\n')


"""
#Otra solucion

line=stdin.readline()
while line!='': 
    array=[]
    i=0
    dim=0
    ant=0
    jolly=True
    for n in line.strip().split():
        dif=abs(int(n)-ant)
        if i==1:
            ant=int(n)
        elif 0<dif<dim:
            if array[dif]!=0:
                jolly=False
                break
            else:
                array[dif]=1
            ant=int(n)
        elif i==0:
            dim=int(n)
            array = [0] * dim
        else:   
            jolly=False
            break
        i=i+1
    if jolly: stdout.write('Jolly\n') 
    else: stdout.write('Not jolly\n')
    line=stdin.readline()


### Otra solucion:


from sys import stdin, stdout

for line in stdin:
    array=[]
    i=0
    dim=0
    ant=0
    jolly=True
    for n in line.strip().split():
        dif=abs(int(n)-ant)
        if i==1:
            ant=int(n)
        elif 0<dif<dim:
            if array[dif]!=0:
                jolly=False
                break
            else:
                array[dif]=1
            ant=int(n)
        elif i==0:
            dim=int(n)
            array = [0] * dim
        else:   
            jolly=False
            break
        i=i+1
    if jolly: stdout.write('Jolly\n') 
    else: stdout.write('Not jolly\n')

"""

#4 1 4 2 3
#5 1 4 2 -1 6


