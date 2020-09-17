from sys import stdin, stdout

array=[0,4,4.5,5,2,1.5]

a, b = [int(n) for n in stdin.readline().strip().split()]

stdout.write('Total: R$ ' + str('{:.2f}'.format(array[a]*b)) + '\n')
