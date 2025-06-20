## Count vowels & consonants in each line of File

fh = open('exercise1.txt','r')
ls = fh.readlines()

for ln in ls:
    v,c=0,0
    for ch in ln:
        if ch in ['a','e','i','o','u']:
            v += 1
        elif ch.isalpha():
            c += 1
    print(ln+"Vowels = "+str(v)+"\nConsonant = "+str(c)+"\n")