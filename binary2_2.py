import pickle

fh = open('temp1.dat','rb')

i = pickle.load(fh)
f = pickle.load(fh)
s = pickle.load(fh)
l = pickle.load(fh)
t = pickle.load(fh)
d = pickle.load(fh)

# cc = pickle.load(fh)

print(i)
print(f)
print(s)
print(l)
print(t)
print(d)

# print(cc)

fh.close()