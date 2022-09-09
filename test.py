

'''
sqrt = lambda a:a**0.5
print(sqrt(81))

'''


'''
sqr = lambda a:a**2
print(sqr(8))


'''


'''
even =  lambda a: a%2 == 0
print(even(56))

'''
'''
sum = lambda a,b,c:a+b+c
print(sum(77,8,9))

'''


'''l = [111,22,113,225]


oddeven = [True if ele%2==0 else False for ele in l]
print(oddeven)
'''

'''n = 98877
l = [int(char) for char in str(n)]
print(l)'''



'''num = 9987

l =[]
while(num>0):
    l.append(num%10)
    num = num//10
print(l[::-1])'''


'''
l=[character for character in 'heY hEy hey u der' if character.lower() in "aeiou"]
print(l)
'''


'''l=[character for character in 'hey hey hey u der']
print(l)

list3=[]
for character in 'hey hey hey u der':
	list3.append(character)

print(list3)
'''










'''list2 = [  [k for k in range(2)]   for j in range(3) for i in range(4)]
print(list2)
l=[]
for j in range(3):
    for i in range(4):
        temp=[]
        for k in range(2):
            temp.append(k)
        l.append(temp)
print(l)
'''
