class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = [[0 for i in range(n)] for i in range(m)]
        paths[0][0] = 1

        for i in range(1, m+n):
            print(paths)
            x = 0
            y = i

            while y >= 0 and x < m:
                if y < n:
                    if x > 0:
                        paths[x][y] += paths[x-1][y]
                    if y > 0:
                        paths[x][y] += paths[x][y-1]

                x += 1
                y -= 1

        
        return paths[m-1][n-1]
                
