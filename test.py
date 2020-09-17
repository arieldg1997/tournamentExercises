from sys import stdin, stdout

s=stdin.readline()
stdout.write('String inicial: '+s)
stdout.write('Lista: '+str(s.strip().split())+'\n')
stdout.write('Strip y Split y join: '+ '-'.join(s.strip().split())+'\n')