## Read above records & show overall % of all students

import csv
f = open('exercise.csv','r')

ro = csv.reader(f, delimiter=',')

ls = list(ro)
print(ls)

sump = 0
n = 0

for r in ls:
    if len(r) > 0:
        print(r)
        sump = sump + float(r[-1])
        n=n+1

print("Overall Percentage: "+ str(sump/n))

f.close()