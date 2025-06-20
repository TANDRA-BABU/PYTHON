## Count lines in a Text File

fh = open('exercise1.txt','r')
ls = fh.readlines()
print(ls, "\nNo of lines = "+str(len(ls)))
fh.close()
