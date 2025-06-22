##Count Char in a Text File

fh = open('exercise1.txt','r')
data = fh.read()
print(data, len(data))
fh.close()