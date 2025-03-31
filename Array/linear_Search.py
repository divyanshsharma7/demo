def linear_search(matrix, target):
    for i in range(len(matrix)):  # Loop through rows
        for j in range(len(matrix[0])):  # Loop through columns
            if matrix[i][j] == target:
                return [i, j]  
    return None  


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

target = 8
result = linear_search(matrix, target)

if result:
    print(f"Element found at index [{result[0]},{result[1]}]")
else:
    print("Element not found.")



# def linear_search(matrix, target):
#     for i in range(len(matrix)):
#         for j in range(len(matrix[0])):
#             if matrix[i][j]==target:
#                 return [i, j]
#     return None
# matrix=[[3,4,6],
#         [7,3,5],
#         [2,1,0]]
# target=0
# result=linear_search(matrix, target)
# if result:
#     print(f"Item found at index [{result[0]}, {result[1]}]")
# else:
#     print("Not found")

