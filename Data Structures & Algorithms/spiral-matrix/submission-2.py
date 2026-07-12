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
                        print("r", uDec, j+lDec)
                        result.append(matrix[uDec][j+lDec])
                    else:
                        print("l", n-1-dDec, m-1-j-rDec)
                        result.append(matrix[n-1-dDec][m-1-j-rDec])

                if direction == 0:
                    uDec += 1
                else:
                    dDec += 1
            else:
                nDec = uDec + dDec
                for i in range(0, n-nDec):
                    if direction == 1:
                        print("d", i+uDec, m-1-rDec)
                        result.append(matrix[i+uDec][m-1-rDec])
                    else:
                        print("u", n-1-i-dDec, lDec)
                        result.append(matrix[n-1-i-dDec][lDec])

                if direction == 1:
                    rDec += 1
                else:
                    lDec += 1

        return result

# [1,2, 3,  4]
# [5,6, 7,  8]
# [9,10,11,12]
# [13,14,15,16]

# 0   j     0 0
# i+1 n     1 0
# n  n-j-1  1 1
# n-i 0     2 1

# 1 j+1     2 2
# i+1 n-1   3 2
# n-1 n-j-2 3 3
# n-i-2 1   4 3

# 2 j+2     4 4
# i+2 n-2
# n-2 n-j-3

