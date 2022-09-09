def myfun(num):
    return num+100

l = [11,22,33,44]

newlist = map(myfun,l)
print(newlist)
print(tuple(newlist))
print(l)
