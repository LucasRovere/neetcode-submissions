class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for i in range(n//2):
                tmp = matrix[i]
                matrix[i] = matrix[n-1-i]
                matrix[n-1-i] = tmp

        for j in range(0, n-1):
            for i in range(j+1, n):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp
