
// PYTHON SOLUTION

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        first_zero_row = False
        first_zero_col = False

#check if first row or first column should be zero
        for j in range(cols):
            if matrix[0][j] == 0:
                first_zero_row = True
        for i in range(rows):
            if matrix[i][0] == 0:
                first_zero_col = True

        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

#zero out based position
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

#first row
        if first_row_zero:
            for j in range(cols):
                matrix[0][j] = 0

#first column
        if first_col_zero:
            for i in range(rows):
                matrix[i][0] = 0