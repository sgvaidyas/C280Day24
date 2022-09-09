


list_numbers = [1, 2, 3, 4]
tuple_numbers = (5, 6, 7, 8,99,77,55)
print(list_numbers)
print(tuple_numbers)

map_iterator = map(lambda x=0, y=0:  x + y, list_numbers, tuple_numbers)
map_list= list(map_iterator)
print(map_list)
