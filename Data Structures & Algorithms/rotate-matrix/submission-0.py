class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for row in range(n):
            for col in range(row + 1, n):
                temp = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = temp
            
        for row in range(n):
            left = 0
            right = n - 1
            while left < right:
                temp = matrix[row][left]
                matrix[row][left] = matrix[row][right]
                matrix[row][right] = temp
                left += 1
                right -= 1
    