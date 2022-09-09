list_numbers = [1, 2, 3, 4]
tuple_numbers = (5, 6, 7, 8)
print(list_numbers)
print(tuple_numbers)

# map function includes a lambda function that calculates the product of two values
map_iterator = map(lambda x, y: x * y, list_numbers, tuple_numbers)

# map output is converted to a list
map_list= list(map_iterator)
print(map_list)
