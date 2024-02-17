file = open('bio.txt','r')
data = file.readlines()
file.close()

print(data)

for line in data:
    line = line.strip()
    key,value = line.split(':')
    value = value.strip()  
    if key == 'age':
        value = int(value)
   
    print(value)