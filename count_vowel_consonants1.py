## Count vowels & consonants in a Text File

fh = open('exercise1.txt','r')
data = fh.read()
v,c=0,0

for ch in data:
    if ch in ['a','e','i','o','u']:
        v += 1
    else:
        c += 1
    
print("Vowels = ",v)
print("Consonant = ",c)