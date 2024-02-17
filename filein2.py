file = open('radius.data','r')
data = file.readlines()
file.close()

print(data)

for r in data:
    r = float(r)
    a = 3.14 * r ** 2
    print(a)