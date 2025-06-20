## Count words in a Text File

fh = open('exercise1.txt','r')
data = fh.read()
ls = data.split()
print(ls, "\nNo of words = "+str(len(ls)))