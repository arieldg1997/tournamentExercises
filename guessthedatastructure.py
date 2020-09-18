from sys import stdin,stdout



for line in stdin:
    stack, queue, pqueue=[],[],[]
    isqueue=True
    ispqueue=True
    isstack=True
    for case in range(int(line.strip())):
        line=stdin.readline().strip().split()
        if line[0]=='1':
            stack.append(int(line[1]))
            queue.append(int(line[1]))
            pqueue.append(int(line[1]))
        elif line[0]=='2':
            if not stack: isstack = False
            if not queue: isqueue = False
            if not pqueue: ispqueue = False
            if isstack:
                if int(line[1])!=stack[len(stack)-1]:
                    isstack=False
                else: stack.pop()
            if isqueue:
                if int(line[1])!=queue[0]:
                    isqueue=False
                else: queue.pop(0)
            if ispqueue:
                if int(line[1])!=max(pqueue):
                    ispqueue=False
                else: pqueue.pop(pqueue.index(max(pqueue)))
    #Como deber me autodejo una forma mas facil de resolver este switch (pensar en enteros)
    if isstack and not isqueue and not ispqueue: stdout.write('stack\n')
    elif not isstack and isqueue and not ispqueue: stdout.write('queue\n')
    elif not isstack and not isqueue and ispqueue: stdout.write('priority queue\n')
    elif not isstack and not isqueue and not ispqueue: stdout.write('impossible\n')
    else: stdout.write('not sure\n')
