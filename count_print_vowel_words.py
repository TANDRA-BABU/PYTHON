## Count Words containing vowels in a file

fh = open('exercise1.txt','r')
data = fh.read()
lw = data.split(' ')

wc=0
for w in lw:
    for ch in w:
        if ch in ['a','e','i','o','u']:
            wc += 1
            break

print(wc)

## also print those words

fh = open('exercise1.txt','r')
data = fh.read()
lw = data.split()
print(lw)
wc=0
for w in lw:
    for ch in w:
        if ch in ['a','e','i','o','u']:
            wc += 1
            print(w)
            break

print(wc)

## Remove \n : data cleaning