class Solution:
    
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if i == 0 and j==0:
                    pass
                elif i==0 and j!=0:
                    
                    grid[i][j] = grid[i][j]+grid[i][j-1]
                elif j==0 and i!=0:
                    
                    grid[i][j] = grid[i][j]+grid[i-1][j]
                else:
                    grid[i][j] = grid[i][j]+min(grid[i][j-1],grid[i-1][j])
        return grid[rows-1][cols-1]
        
    
        
