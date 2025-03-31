def spiral_traversal(matrix):
    res = []
    if not matrix:  # If matrix is empty, return empty list
        return res

    row_begin, row_end = 0, len(matrix) - 1
    col_begin, col_end = 0, len(matrix[0]) - 1

    while row_begin <= row_end and col_begin <= col_end:
        # Traverse from left to right
        for i in range(col_begin, col_end + 1):
            res.append(matrix[row_begin][i])
        row_begin += 1

        # Traverse from top to bottom
        for i in range(row_begin, row_end + 1):
            res.append(matrix[i][col_end])
        col_end -= 1

        # Traverse from right to left
        if row_begin <= row_end:
            for i in range(col_end, col_begin - 1, -1):
                res.append(matrix[row_end][i])
            row_end -= 1

        # Traverse from bottom to top
        if col_begin <= col_end:
            for i in range(row_end, row_begin - 1, -1):
                res.append(matrix[i][col_begin])
            col_begin += 1

    return res


# Input Matrix
matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]


result = spiral_traversal(matrix)


print(result)
