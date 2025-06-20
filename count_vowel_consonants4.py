## Count vowels & consonants in a Text File

def count_v_c():
fh = open('exercise1.txt','r')
data = fh.read()
v,c=0,0
vowels = ['a','e','i','o','u']
for ch in data:
    if ch in vowels:
        v += 1
    elif ch.isalpha():
        c += 1
    
print("Vowels = ",v)
print("Consonant = ",c)

count_v_c()