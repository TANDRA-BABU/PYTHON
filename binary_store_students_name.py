## Store a List of student names in Binary File

import pickle

fh = open('students_name.txt','wb')

no = int(input("no. of students: "))

ln =[]

for i in range(no):
    ln.append(input('Enter Name: '))

pickle.dump(ln,fh)

fh = open('students_name.txt','rb')

ln = pickle.load(fh)

print(ln)

fh.close()