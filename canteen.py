from sys import stdin, stdout


cases=int(stdin.readline().strip())
for _ in range(cases):
    n_students=int(stdin.readline().strip())
    cant=0
    grades=(list([int(n) for n in stdin.readline().strip().split()]))
    aux_grades=grades.copy()
    aux_grades.sort(reverse=True)
    for i in range(len(grades)):
        if grades[i]==aux_grades[i]: 
            cant+=1
    stdout.write(str(cant)+'\n')