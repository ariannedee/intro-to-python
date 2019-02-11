# Indexing and slicing
new_list = [0, 1, 2, 3]

print(new_list[1])
print(new_list[1:3])
print(new_list[:2])
print(new_list[2:])
print()


# Adding, removing, and updating
movies = ['Blindspoting', 'Black Panther', 'Annihilation']

movies[0] = 'Blindspotting'
movies.append('Sorry to Bother You')                # Adds item to end of list
movies.insert(1, 'Won\'t You Be My Neighbour')      # Adds item to list at index
movies.remove('Annihilation')
print(movies)


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
