#linear search in python
a = []

def linearsearch(a, search, helement):
    flag = False
    for x in range(helement):
        if a[x] == search:
            flag = True
            pos = x+1
            break
    if flag:
        print(f'search item found {pos} position')
    else:
        print('search item not found')


helement = int(input("how much element you enter : "))

for i in range(helement):
    element1 = input("input element : ")
    a.append(element1)
search = input("please input search item : ")
linearsearch(a, search, helement)
