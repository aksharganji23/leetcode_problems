class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        neg=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]<0:
                    neg+=1
        return (neg)
