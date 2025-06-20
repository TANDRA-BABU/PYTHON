import pickle

fh = open('temp1.dat','wb')

i = 10
f = 1.1
s = 'hello'
l = [1,2,3]
t = (5,6,7)
d = {1:'a',2:'b'}

pickle.dump(i,fh)
pickle.dump(f,fh)
pickle.dump(s,fh)
pickle.dump(l,fh)
pickle.dump(t,fh)
pickle.dump(d,fh)

fh.close()