# ========================= Question =========================
#
# You are given a matrix with R rows and C columns.
#
# Calculate the sum of every row and every column.
#
# Example:
#
# Input:
# 2 3
# 1 2 3
# 4 5 6
#
# Output:
# Row sums: 6 15
# Column sums: 5 7 9
#
# Important Points:
#
# 1. Read the number of rows R and columns C.
# 2. Read the matrix values.
# 3. Initialize a list for row sums.
# 4. Initialize a list for column sums.
# 5. Use nested loops to visit every element.
# 6. Add each element to its row's sum.
# 7. Add each element to its column's sum.
# 8. Print the row sums and column sums.
#
# ============================================================


# ======================= Solution ===========================
def calculate_sums(matrix):
    rows = len(matrix)
    columns = len(matrix[0])

    row_sums = [0] * rows
    column_sums = [0] * columns

    for i in range(rows):
        for j in range(columns):
            row_sums[i] += matrix[i][j]

            column_sums[j] += matrix[i][j]

    print("Row sums:", *row_sums)
    print("Column sums:", *column_sums)


if __name__ == '__main__':
    rows, columns = map(int, input().split())
    
    matrix = []
    for i in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)

    calculate_sums(matrix)
