from sys import stdin,stdout


dictionary={}
for line in stdin:
    line=line.strip().split()
    if not line:
        break
    for element in line:
        if element not in dictionary.keys(): 
            dictionary[element]=0
        dictionary[element]+=1

for element in dictionary:
    stdout.write(str(element)+' '+str(dictionary[element])+'\n')
