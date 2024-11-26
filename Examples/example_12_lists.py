# Indexing and slicing
new_list = [0, 1, 2, 3]

print(new_list[1])
print(new_list[1:3])
print(new_list[:2])
print(new_list[2:])
print()


# Adding, removing, and updating
languages = ['English', 'French', 'Mandarin']

languages[0] = 'Icelandic'
languages.append('Tagalog')     # Adds item to end of list
languages.insert(1, 'Spanish')  # Adds item to list at index
languages.remove('Mandarin')
print(languages)


# More list methods
new_list.insert(1, True)  # Lists can hold any type of data
new_list.extend([1, 2, 3])
print(new_list)
new_list.reverse()
print(new_list)
print(new_list.count(1))  # Remember, 1 == True
new_list.sort()
print(new_list)


# Nested lists can be used for matrices
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

matrix[1][0] = 1000
print(matrix)
