## Copy Data from file_a to file_b & add line numbers in file_b

fh_a = open('file_a.txt','r')
fh_b = open('file_b.txt','w')

ls = fh_a.readlines()

i=1
for ln in ls:
    fh_b.write(str(i)+". "+ln)
    i+=1

fh_a.close()
fh_b.close()