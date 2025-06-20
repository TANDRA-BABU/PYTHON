## Append few more student records to above file
##WRITEROW
import csv
f = open('exercise.csv','a')

wo = csv.writer(f, delimiter=',')

n = int(input('Enter no. of Students: '))

lr =[]   # list of records

for i in range(n):
    rn = int(input('Enter Roll No: '))
    nm = input('Enter Name: ')
    a = int(input('Enter Age: '))
    c = input('Enter Class: ')
    p = float(input('Enter Percentage: '))
    wo.writerow([rn,nm,a,c,p])

f.close()