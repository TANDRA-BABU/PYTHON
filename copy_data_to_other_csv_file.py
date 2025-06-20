## Copy above data to another csv file after giving 5% extra to all

import csv

fa = open('exercise.csv','r')
fb = open('extra-05.csv','w')

ro = csv.reader(fa, delimiter=',')
wo = csv.writer(fb, delimiter=',')

ls = list(ro)

for r in ls:
    if len(r) > 0:
        nl = r[0:4] + [float(r[-1])+5]
        print(nl)
        wo.writerow(nl)

fa.close()
fb.close()