class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        newarr=[]
        m = len(obstacleGrid)
        n=len(obstacleGrid[0])
        if m==1 and n==1:    # when there is a single element in given matrix
            if obstacleGrid[0][0]==0:
                return 1
            else:
                return 0
        if obstacleGrid[0][0]==1:           # when we have obstacle at index 0,0
            return 0
        
        lis=[]
        for i in range(m):                  # creating new matrix whole last index will give us our answer
            lis.clear()
            for j in range(n):
                lis.append(0)
            newarr.append(lis)
        
        columnupdater=True                  # it will work like a switch for column number 0 initially it is on means column 0 values can be updated once it is off then upcoming column 0 vallues will always bee false
        
        rowupdater=True                     # same concept of switch is used her also for row 0 elements
        
        for i in range(m):
            
            for j in range(n):
                if i==0 and j==0:
                    newarr[0][0]=0
                elif i==0 and rowupdater:
                    if obstacleGrid[0][j-1]==1 or obstacleGrid[0][j]==1:
                        newarr[0][j]=0
                        rowupdater=False
                    else:
                        newarr[0][j]=1
                elif j==0 and columnupdater:
                    if obstacleGrid[i-1][0]==1 or obstacleGrid[i][0]==1:
                        newarr[i][0]=0
                        columnupdater=False
                    else:
                        newarr[i][0]=1
                elif i!=0 and j!=0:
                    if (newarr[i][j-1]!=0 or newarr[i-1][j]!=0) and obstacleGrid[i][j]!=1:
                        newarr[i][j]=newarr[i-1][j]+newarr[i][j-1]
                    else:
                        newarr[i][j]=0
                    
                
                
        
        return newarr[m-1][n-1]
