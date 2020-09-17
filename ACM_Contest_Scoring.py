from sys import stdin, stdout

answers={}
correct_answers=[]
cont=0
for line in stdin:
    if line=='-1\n':    
        stdout.write(str(len(correct_answers))+' '+str(cont)+'\n')
        cont=0
        answers={}
        correct_answers=[]
        continue 
    if line=='\n':
        break
    line=line.strip().split()
    if line[1] not in answers.keys():
        if line[2]=='wrong': answers[line[1]]=20    
        else:
            answers[line[1]]=0 
            cont+=int(line[0])
    elif line[1] not in correct_answers:
        if line[2]=='wrong': answers[line[1]]+=20    
        else: cont=cont+int(line[0])+answers[line[1]]
    if line[2]=='right': correct_answers.append(line[1])


"""
3 E right
10 A wrong
30 C wrong
50 B wrong
100 A wrong
200 A right
250 C wrong
300 D right
-1
7 H right
15 B wrong
30 E wrong
35 E right
80 B wrong
80 B right
100 D wrong
100 C wrong
300 C right
300 D wrong
-1
"""