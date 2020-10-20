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

