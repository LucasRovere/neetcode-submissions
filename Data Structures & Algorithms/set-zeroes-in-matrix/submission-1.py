class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])
        zeroColumns = []

        for i in range(n):
            helperSet = set(matrix[i])
            if 0 in helperSet:
                for j in range(m):
                    if matrix[i][j] == 0:
                        zeroColumns.append(j)
                    else:
                        matrix[i][j] = 0
        
        for i in range(n):
            if matrix[i][0] == 0:
                continue
            else:
                for j in zeroColumns:
                    matrix[i][j] = 0
        