## Count alphabets, digits, spaces & special char in a Text File

fh = open('exercise1.txt','r')
data = fh.read()
a,d,s,sc = 0,0,0,0
for ch in data:
    if ch.isalpha():
        a += 1 
    elif ch.isdecimal():
        d += 1
    elif ch.isspace():
        s += 1
    else:
        sc += 1
print("Alphabet = ",a)  
print("Digits = ",d)  
print("Spaces = ",s)  
print("Special Character = ",sc)