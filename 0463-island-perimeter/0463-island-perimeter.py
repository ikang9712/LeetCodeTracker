class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        res = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    res += 4
                    # check top 
                    if i > 0 and grid[i-1][j] == 1:
                        res -= 2
                    # check left 
                    if j > 0 and grid[i][j-1] == 1:
                        res -= 2
        return res

            