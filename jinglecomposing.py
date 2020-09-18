from sys import stdin, stdout


notes={'W':1,'H':1/2,'Q':1/4,'E':1/8,'S':1/16,'T':1/32,'X':1/64}
for line in stdin:
    if line=='*\n':
        break
    line=line.strip().split('/')
    right=0
    for l in line:
        cant=0
        for char in l:
            cant+=notes[char]
            if cant>1: break
        if cant==1:
            right+=1
    stdout.write(str(right)+'\n')

