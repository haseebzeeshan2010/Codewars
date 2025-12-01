# Find all the saddle points of a non-empty matrix of integers. A saddle point is an element that is minimal in its row and maximal in its column. Return them in a list of (row,column) coordinates. The order of the saddle points in the list is irrevelant.

# Example
# Consider the following matrix:

# 6 4 3
# 7 0 2
# 4 3 2
# 5 3 3
# The row minimums are 3, 0, 2, 3 (at positions 1 and 2).
# The column maximums are 7, 4, 3 (at positions 0 and 3).
# Therefore the 3's in the 3rd column are saddle points, but the 3's in the 2nd column are not.
# Return [(0,2), (3,2)]] or [(3,2), (0,2)].
# Constraints
# Number of rows r and number of columns c satisfy1 ≤ r,c ≤ 500. So you should think about efficiency (a little).

#MY SOLUTION
def find_saddle_points(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    col_max = [float('-inf')] * cols
    for j in range(cols):
        for i in range(rows):
            if matrix[i][j] > col_max[j]:
                col_max[j] = matrix[i][j]

    saddle_points = []
    for i, row in enumerate(matrix):
        row_min = float('inf')
        min_positions = []

        
        for j, val in enumerate(row):
            if val < row_min:
                row_min = val
                min_positions = [j]
            elif val == row_min:
                min_positions.append(j)


        for j in min_positions:
            if row[j] == col_max[j]:
                saddle_points.append((i, j))

    return saddle_points


#BEST SOLUTION - by anter69
def find_saddle_points(matrix):
    columns = list(zip(*matrix))
    min_row = list(map(min, matrix))
    max_col = list(map(max, columns))
    
    return [ (row, col)
            for row in range(len(matrix))
                for col in range(len(columns))
                    if min_row[row] == max_col[col]
        ]