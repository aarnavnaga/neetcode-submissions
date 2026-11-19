from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        columns = len(matrix[0])
        original_zeroes = []

        for row in range(rows):
            for col in range(columns):
                if matrix[row][col] == 0:
                    original_zeroes.append((row, col))

        for row, column in original_zeroes:
            for current_col in range(columns):
                matrix[row][current_col] = 0
            for current_row in range(rows):
                matrix[current_row][column] = 0

# O(mn + k(m + n))
