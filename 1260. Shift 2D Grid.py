class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        if k==0:
            return grid
        lis=[]
        for p in range(k):
            n = len(grid[0])
            m = len(grid)
            lis = [[0 for i in range(n)] for j in range(m)]
            for i in range(m):
                for j in range(n):
                    if i==m-1 and j==n-1:
                        lis[0][0]=grid[i][j]
                    elif j==n-1:
                        lis[i+1][0]=grid[i][n-1]
                    else:
                        lis[i][j+1]=grid[i][j]
            grid = lis.copy()
        return lis
                    
