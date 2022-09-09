def remove_first_char(s):
    return s[1:]

names=['haythem','mike','james']
print(names)

names_new = map(remove_first_char, names)
names_new_list = list(names_new)
print(names_new_list)
