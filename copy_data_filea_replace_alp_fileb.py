## Copy Data from file_a to file_b after replacing alphabets with '*', digits with '#', spaces with '_'

fh_a = open('file_a.txt','r')
fh_b = open('file_b.txt','w')

data = fh_a.read()

for ch in data:
    if ch.isalpha():
        fh_b.write('*')
    elif ch.isdecimal():
        fh_b.write('#')
    elif ch.isspace():
        fh_b.write('_')
    else:
        fh_b.write(ch)

print(data)

    
fh_a.close()
fh_b.close()