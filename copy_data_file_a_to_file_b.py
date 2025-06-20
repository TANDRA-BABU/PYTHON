## Copy Data from file_a to file_b

fa = open(r'file_a.txt','r')
fb = open(r'file_b.txt','w')
data = fa.read()
fb.write(data)
fa.close()
fb.close()