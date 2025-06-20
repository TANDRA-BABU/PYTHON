## Write records of students (rn, name, age, class, %) in CSV file
##WRTEROWS
import csv
f = open('exercise.csv','w')

wo = csv.writer(f, delimiter=',')

n = int(input('Enter no. of Students: '))

lr =[]   # list of records

for i in range(n):
    rn = int(input('Enter Roll No: '))
    nm = input('Enter Name: ')
    a = int(input('Enter Age: '))
    c = input('Enter Class: ')
    p = float(input('Enter Percentage: '))
    lr.append([rn,nm,a,c,p])

wo.writerows(lr)
f.close()