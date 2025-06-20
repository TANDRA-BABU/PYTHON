## Read file_a & write each word in separate line in file_b

fh_a = open('file_a.txt','r')
fh_b = open('file_b.txt','w')

data = fh_a.read()
fw = data.split()

print(fw)

for w in fw:
    fh_b.write(w+"\n")

fh_a.close()
fh_b.close()