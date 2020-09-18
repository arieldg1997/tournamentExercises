from sys import stdin, stdout


s=set()
a, b = [int(n) for n in stdin.readline().strip().split()]
while a!=0 and b!=0:
    s.clear()
    cont=0
    for I in range(a):
        s.add(int(stdin.readline().strip()))
    for J in range(b):
        if int(stdin.readline().strip()) in s: cont+=1
    stdout.write(str(cont)+'\n')
    a, b = [int(n) for n in stdin.readline().strip().split()]