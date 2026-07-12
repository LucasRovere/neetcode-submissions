class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        iterations = 2 * min(n, m)

        uDec = 0
        lDec = 0
        dDec = 0
        rDec = 0

        result = []

        for it in range(iterations):
            direction = it % 4

            if direction % 2 == 0:
                mDec = lDec + rDec
                for j in range(0, m-mDec):
                    if direction == 0:
                        result.append(matrix[uDec][j+lDec])
                    else:
                        result.append(matrix[n-1-dDec][m-1-j-rDec])

                if direction == 0:
                    uDec += 1
                else:
                    dDec += 1
            else:
                nDec = uDec + dDec
                for i in range(0, n-nDec):
                    if direction == 1:
                        result.append(matrix[i+uDec][m-1-rDec])
                    else:
                        result.append(matrix[n-1-i-dDec][lDec])

                if direction == 1:
                    rDec += 1
                else:
                    lDec += 1

        return result


