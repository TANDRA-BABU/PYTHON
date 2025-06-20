## Copy Data from file_a to file_b & Capital all letters

fh_a = open('file_a.txt','r')
fh_b = open('file_b.txt','w')

data = fh_a.read()

fh_b.write(data.upper())

#fh_b.write(data.lower())

#fh_b.write(data.capitalize())

#fh_b.write(data.title())
    
fh_a.close()
fh_b.close()