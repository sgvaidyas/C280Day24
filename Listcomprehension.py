list = [i for i in range(20) if i % 2 == 0]
print(list)



list2 = [[j for j in range(4)] for i in range(4)]
print(list2)


# Empty list
list3 = []

# Traditional approach of iterating
for character in 'hey hey hey u der':
	list3.append(character)

# Display list
print(list3)


# Using list comprehension to iterate through loop
list4 = [character for character in 'today is friday']

# Displaying list
print(list4)
