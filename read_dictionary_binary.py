## Read the Dictionary

import pickle
fh = open('exercise1.txt','rb')
ln = pickle.load(fh)
d = pickle.load(fh)
print(ln)
print(d)
fh.close()