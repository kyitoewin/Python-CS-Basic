file = open('radius.data','r')
data = file.readlines()
file.close()

print(data)

area_file = open('area.data','w')
for r in data:
    r = float(r)
    a = 3.14 * r ** 2
    a = str(a)
    area_file.write(f'radis = {r} cm , area = {a} sqcm \n')
    print(a)
area_file.close()