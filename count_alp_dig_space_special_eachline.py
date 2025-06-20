## Count alphabets, digits, spaces & special char in each line of File

fh = open('exercise1.txt','r')
ls = fh.readlines()

for ln in ls:
    a,d,s,sc = 0,0,0,0
    for ch in ln:
        if ch.isalpha():
            a += 1 
        elif ch.isdecimal():
            d += 1
        elif ch.isspace():
            s += 1
        else:
            sc += 1
    print("\n"+ln)
    print("Alphabet = ",a)  
    print("Digits = ",d)  
    print("Spaces = ",s)  
    print("Special Character = ",sc)