def contains_e(dataset):
    for x in dataset:
        if "e" in x:
            return x

names=['Haythem','Mike','James','Helen','Mary']
print(names)

names_filtered = filter(contains_e,names)
print(type(names_filtered))

names_filtered_list = list(names_filtered)
print(type(names_filtered_list))

print(names_filtered_list)
