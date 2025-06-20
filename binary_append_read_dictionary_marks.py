### Append a Dictionary of student marks to the above file_handle


import pickle

fh = open('exercise.txt','rb')
ln = pickle.load(fh)
print(ln)
fh.close()




fh = open('exercise.txt','ab')
d ={}
for nm in ln:
    d[nm] = float(input(f'Enter Marks for {nm}: '))

pickle.dump(d,fh)

## Read the Dictionary

# import pickle
# fh = open('exercise.txt','rb')
ln = pickle.load(fh)
d = pickle.load(fh)
print(ln)
print(d)

# fh.close()
fh.close()