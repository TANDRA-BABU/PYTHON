## Read file_a & write no. of words in file_b

fh_a = open('file_a.txt','r')
fh_b = open('file_b.txt','w')

data = fh_a.read()
fw = data.split()

fh_b.write("no of words in file_a have "+ str(len(fw)))

fh_a.close()
fh_b.close()