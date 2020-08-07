
array = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

print(array)
print(list(zip(*array)))
print(list(zip(*array[::-1])))
