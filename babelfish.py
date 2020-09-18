from sys import stdin,stdout


dictionary={}
for line in stdin:
    line=line.strip().split()
    if not line:
        break
    dictionary[line[1]]=line[0]

for line in stdin:
    line=line.strip()
    if not line:
        break
    if line in dictionary.keys():
        stdout.write(str(dictionary[line])+'\n')
    else:
        stdout.write('eh\n')

