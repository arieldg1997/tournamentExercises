from sys import stdin, stdout
import math

"""

#Primera solucion

cases=int(stdin.readline())
cases_results=[]
for I in range(cases):
    days=[0] * int(stdin.readline())
    not_working_days=[]
    k=0
    while len(days)>5+7*k:
        not_working_days.append(5+7*k)
        if len(days)>6+7*k:
            not_working_days.append(6+7*k)   
        k+=1  
    for J in range(int(stdin.readline())):
        hartal_parameter=int(stdin.readline())
        for Z in range(math.floor(len(days)/hartal_parameter)):
            index=hartal_parameter*(Z+1)-1
            if index not in not_working_days:
                days[hartal_parameter*(Z+1)-1]=1
    cases_results.append(days.count(1))
for N in cases_results:
    stdout.write(str(N)+'\n')

"""

#Segunda solucion

cases=int(stdin.readline())
cases_results=[]
for I in range(cases):
    days=[0] * int(stdin.readline())
    for J in range(int(stdin.readline())):
        hartal_parameter=int(stdin.readline())
        for Z in range(math.floor(len(days)/hartal_parameter)):
            days[hartal_parameter*(Z+1)-1]=1
    k=0
    while len(days)>5+7*k:
        days[5+7*k]=0
        if len(days)>6+7*k:
            days[6+7*k]=0 
        k+=1  
    cases_results.append(days.count(1))
for N in cases_results:
    stdout.write(str(N)+'\n')


'''
Input:
2
14
3
3
4
8
100
4
12
15
25
40

Output:
5
15
'''

